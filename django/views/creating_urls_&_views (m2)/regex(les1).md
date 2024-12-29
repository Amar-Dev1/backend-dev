# Django Regular Expressions for Dynamic URLs

Regular expressions (regex) allow you to create dynamic URLs that can match patterns in the URL string.

To use regular expressions in Django URLs, you need to import `re_path` from `django.urls`.

```python
from django.urls import path, re_path

urlpatterns = [
     path('menu_item/<int:id>', views.books),  # <- not regex ❌
     re_path(r'^menu_item/([0-9]{2})/$', views.display_menu_item),  # <- regex ✅
]
```

## The URLs for `r'^menu_item/([0-9]{2})/$'`

- `/menu_item/03` ✅
- `/menu_item/123` ❌


# Regex Demonstration

- **r** (raw string):  
  Treats symbols as string characters, not escape characters.

- **^**:  
  Anchors the regex to the start of the string.

- **$**:  
  Anchors the regex to the end of the string.

- **{2}**:  
  Specifies the number of characters (in this case, 2).
