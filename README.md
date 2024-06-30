# Installation

```bash
pip install django-simple-editorjs
```

# Setup

```python
# settings.py
INSTALLED_APPS = [
    ...
    'django_simple_editorjs',
]

```

# Example

```python
# models.py
from django.db import models
from django_simple_editorjs import EditorJsField

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = EditorJsField()
```