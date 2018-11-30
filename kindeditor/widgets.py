from django import forms
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.utils import flatatt
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.functional import Promise
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.utils.translation import get_language


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)
        return super().default(obj)


json_encode = LazyEncoder().encode

DEFAULT_CONFIG = {}


class KindeditorWidget(forms.Textarea):
    """
    Widget providing kindeditor for Rich Text Editing.
    Supports direct image uploads and embed.
    """

    class Media:
        js = (
            "kindeditor/kindeditor-all.min.js",
            "kindeditor/lang/zh-CN.min.js",
            "kindeditor/config.min.js",
        )

    def __init__(
        self,
        config_name="default",
        extra_plugins=None,
        external_plugin_resources=None,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.config = DEFAULT_CONFIG.copy()
        self.external_plugin_resources = external_plugin_resources or []

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ""
        final_attrs = self.build_attrs(self.attrs, attrs, name=name)
        self._set_config()
        external_plugin_resources = [
            [force_text(a), force_text(b), force_text(c)]
            for a, b, c in self.external_plugin_resources
        ]
        return mark_safe(
            render_to_string(
                "kindeditor/widget.html",
                {
                    "final_attrs": flatatt(final_attrs),
                    "value": conditional_escape(force_text(value)),
                    "id": final_attrs["id"],
                    "config": json_encode(self.config),
                    "external_plugin_resources": json_encode(
                        external_plugin_resources
                    ),
                },
            )
        )

    def build_attrs(self, base_attrs, extra_attrs=None, **kwargs):
        attrs = dict(base_attrs, **kwargs)
        if extra_attrs:
            attrs.update(extra_attrs)
        return attrs

    def _set_config(self):
        lang = get_language()
        if lang == "zh-hans":
            lang = "zh-cn"
        self.config["language"] = lang
