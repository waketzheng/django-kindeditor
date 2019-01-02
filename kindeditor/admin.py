from django.contrib import admin


class EditorAdminMixin:
    class Media:
        js = (
            "kindeditor/kindeditor-all.min.js",
            "kindeditor/lang/zh-CN.min.js",
            "kindeditor/config.min.js",
        )


class EditorAdmin(admin.ModelAdmin, EditorAdminMixin):
    pass
