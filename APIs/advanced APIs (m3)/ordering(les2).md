# 📑 Ordering & Sorting

- 💡since we deal with function based views via `@api_vew` decorator we can use django ntive sorting methods.

## Implement sorting 
1. retrive ordering query parameter.
```python
ordering = request.query_params.get('ordering')
```
2. add order logic (befor serilaizer line)
```python
if ordering:
    items = items.order_by(ordering)
```
3. type the the url endpoint in browser
```http
http://localhost/api/menu-items/?ordering=price

# this return items ordered based on price (Asending)
```

## 💡 Note
- the `ordering` function by default do **Asending**
- to make it **Desending**. `http://localhost/api/menu-items/?ordering=-price`

## 💡 Ordering with multiple fields
1. create list hold the ordering fields
```python 
if ordering:
    ordering_fields = ordering.split(',')
    items = items.order_by(*ordering_fields)
```
```http
http://localhost/api/menu-items/?ordering=price,inventory

# this sorting by price first and then by inventory (Asending)
```