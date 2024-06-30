from django.template import loader
from django.db import models
from django import forms

class EditorJsWidget(forms.widgets.Textarea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def media(self):
        return forms.Media(
            css = {
                "all": [
                    "django-simple-editorjs/main.css",
                ]
            },
            js = [
                "django-simple-editorjs/tools/header.js",
                "django-simple-editorjs/tools/simple-image.js",
                "django-simple-editorjs/tools/delimiter.js",
                "django-simple-editorjs/tools/list.js",
                "django-simple-editorjs/tools/checklist.js",
                "django-simple-editorjs/tools/quote.js",
                "django-simple-editorjs/tools/code.js",
                "django-simple-editorjs/tools/embed.js",
                "django-simple-editorjs/tools/table.js",
                "django-simple-editorjs/tools/link.js",
                "django-simple-editorjs/tools/warning.js",
                "django-simple-editorjs/tools/marker.js",
                "django-simple-editorjs/tools/inline-code.js",
                "django-simple-editorjs/main.js",
            ],
        )
    
    def render(self, name, value, **kwargs):
        return loader.render_to_string("django-simple-editorjs/main.html", {"name": name, "id": kwargs["attrs"]["id"], "value": value })

class EditorJsField(models.Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_internal_type(self):
        return "TextField"
    
    def formfield(self, *args, **kwargs):
        kwargs["widget"] = EditorJsWidget()
        return super().formfield(*args, **kwargs)