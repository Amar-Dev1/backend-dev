# 📑Pagination
- 💡is a way we can junk the api content based on client request
- 💡we can use pagination to limit the number of items returned in a response

## 📑How to use it
1. retrive `perpage` and `page` from `query_params`.
```python
perpage = request.query_params.get('perpage',default=2)
page = request.query_params.get('page',default=1)
```
2. import `Paginator` and `EmptyPage` from `django.core.paginator`
```python
from django.paginator import Paginator, EmptyPage
```
3. before serializered item add the instance of `Paginator`
```python
paginator = Paginator(items,per_page=perpage)
try:
    items = paginator.page(page)
except EmptyPage:
    items = []   
```

## 💡 Notes
- 💡 `perpage` is the number of items (records) to be returned in a response.
- 💡 `page` is the current page number.
- 💡 `Paginator` is a class that helps us to paginate the items.
- 💡 `EmptyPage` is a class that helps us to handle the case when the pag request is empty.

## 📑Example for endpoints :
- 💡return page number 4 with 2 items
```http
http://127.0.0.1:8000/api/menu-items/?perpage=2&page=4
```
- 💡return page number 3 with 2 items
```http
http://127.0.0.1:8000/api/menu-items/?perpage=2&page=3
```