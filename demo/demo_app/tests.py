import hashlib
import os
from datetime import datetime
from time import sleep

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.staticfiles.finders import find
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from selenium import webdriver

from kindeditor.models import DEFAULT_UPLOAD_TO

CHROMIUM = "chromium"
FIREFOX = "firefox"
SELENIUM_BROWSER = os.getenv("SELENIUM_BROWSER", CHROMIUM)


class TestAdminPanelWidget(StaticLiveServerTestCase):
    fixtures = ["test_admin.json"]

    @classmethod
    def setUpClass(cls):
        if SELENIUM_BROWSER == CHROMIUM:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            cls.selenium = webdriver.Chrome(chrome_options=options)
        elif SELENIUM_BROWSER == FIREFOX:
            cls.selenium = webdriver.Firefox()
        super(TestAdminPanelWidget, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(TestAdminPanelWidget, cls).tearDownClass()

    def test_admin_panel_widget(self):
        self._login_to_admin()
        self._go_to_demo_application_in_admin()
        self._assert_editor_loaded()
        self._enter_title_text()
        self._focus_cursor_in_editor()
        self._enter_test_text()
        self._open_image_upload_widget()
        self._go_to_upload_tab()
        # self._switch_to_form_iframe()
        self._upload_image()
        self._assert_image_uploaded()

    def _login_to_admin(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/admin/"))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("test")
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("test")
        input_value = _("Log in")
        login_btn = f'//input[@value="{input_value}"]'
        self.selenium.find_element_by_xpath(login_btn).click()

    def _go_to_demo_application_in_admin(self):
        self.selenium.get(
            "%s%s" % (self.live_server_url, "/admin/demo_app/article/add/")
        )

    def _assert_editor_loaded(self):
        sleep(2)
        self.selenium.find_element_by_class_name("django-kindeditor-widget")

    def _enter_title_text(self):
        self.selenium.find_element_by_id("id_title").send_keys("test")

    def _focus_cursor_in_editor(self):
        self.frame = self.selenium.find_element_by_class_name("ke-edit-iframe")
        self.frame.click()

    def _enter_test_text(self):
        self.frame.send_keys("test")

    def _open_image_upload_widget(self):
        self.selenium.find_element_by_css_selector(
            "span.ke-toolbar-icon.ke-toolbar-icon-url.ke-icon-image"
        ).click()
        sleep(1)

    def _go_to_upload_tab(self):
        self.selenium.find_element_by_css_selector(
            "li[class='ke-tabs-li']"
        ).click()
        sleep(1)

    def _switch_to_form_iframe(self):
        iframe = self.selenium.find_element_by_css_selector(
            "iframe.kindeditor_upload_iframe_1543521470827"
        )
        self.selenium.switch_to.frame(iframe)

    def _upload_image(self):
        input = self.selenium.find_element_by_class_name("ke-upload-file")
        input.send_keys(self._get_upload_file())
        self.selenium.switch_to.default_content()
        self.selenium.find_element_by_css_selector(
            # "input[class='ke-button-common ke-button']"
            "span[class='ke-button-common ke-button-outer ke-dialog-yes']"
        ).click()
        sleep(2)

    def _get_upload_file(self):
        return find("kindeditor/plugins/image/images/refresh.png")

    def _assert_image_uploaded(self):
        upload_directory = self._get_upload_directory()
        expected_image_path = os.path.join(upload_directory, "refresh.png")
        assert os.path.isfile(expected_image_path)
        self._assert_uploaded_image_did_not_changed(expected_image_path)
        os.remove(expected_image_path)

    def _get_upload_directory(self):
        uploadto = getattr(settings, "KINDEDITOR_UPLOAD_TO", DEFAULT_UPLOAD_TO)
        upload_path = datetime.now().strftime(uploadto)
        return os.path.join(settings.MEDIA_ROOT, upload_path)

    def _assert_uploaded_image_did_not_changed(self, path):
        expected_sha = self._get_sha1_for_file(self._get_upload_file())
        uploaded_sha = self._get_sha1_for_file(path)
        assert expected_sha == uploaded_sha

    def _get_sha1_for_file(self, path):
        image = open(path, "rb")
        hash = hashlib.sha1()
        hash.update(image.read())
        return hash.hexdigest()


class BaseUploadTest(TestCase):
    pass

class UploadPermissionTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = reverse("kindeditor-image-upload")
        User = get_user_model()
        cls.superuser = {"username": "super", "password": "123"}
        cls.user = {"username": "user", "password": "321"}
        User.objects.create_superuser(**cls.superuser, email='')
        User.objects.create_user(**cls.user)
        super().setUpClass()

    def setUp(self):
        img = "kindeditor/plugins/image/images/refresh.png"
        img = os.path.join(settings.BASE_DIR, "kindeditor/static", img)
        self.data = {"img": open(img, "rb")}
    
    @override_settings(KINDEDITOR_UPLOAD_PERMISSION=None)
    def test_none_permission(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 201)

    @override_settings(KINDEDITOR_UPLOAD_PERMISSION='login')
    def test_authenticate_required(self):
        response = self.client.post(self.url, self.data)
        print('-'*20)
        print(response.json())
        print('-'*20)
        print('permission:')
        print(settings.KINDEDITOR_UPLOAD_PERMISSION)
        self.assertEqual(response.status_code, 400)
        self.client.login(**self.user)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 201)

    @override_settings(KINDEDITOR_UPLOAD_PERMISSION='admin')
    def test_admin_required(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 400)
        self.client.login(**self.user)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 400)
        self.client.login(**self.superuser)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 201)
