from django.contrib import admin


class EditorAdmin(admin.ModelAdmin):
    class Media:
        js = (
            "kindeditor/kindeditor-all.min.js",
            "kindeditor/lang/zh-CN.min.js",
            "kindeditor/config.min.js",
        )
