# 📑 Filtering & Searching using APIs

## 🔵 Two ways to implement filter & search:
### 1. implement it on the client (not efficient)
- 💡 fetch all the data and then apply the filtering or searching (for every request !).
- 💡 create a heavy load on the server.

### 2. implement it on the server-side
- 💡less load, less time on the server (cuz all the filtering done on server-side)

## 📑Examples of filtering endpoints
1. api for items from **icecream** category
```http
http://127.0.0.1:8000/api/menu-items/?category=icecream
```
2. api for items in price range (0$ to 5$)
```http
http://127.0.0.1:8000/api/menu-items/?to_price=5
```
3. api for icecream items and the price in (0$ to 5$)
```http
http://127.0.0.1:8000/api/menu-items/?category=icecream&to_price=5
```

## 💡 Some filter commands 
- `lte` : `items.filter(price__lte=to_price)` (less than or equal)
- `gte` : `items.filter(price__gte=to_price)` (greater than or equal)
- `lt` : `items.filter(price__lt=to_price)` (less than)
- `gt` : `items.filter(price__gt=to_price)` (greater than)
- `in` : `items.filter(category__title__in=[category_name1, category_nam])

## 💡 Some search commands
- `contains` : `items.filter(title__contains='icecream')` (search for items contain `icecream`)
- `startswith` : `items.filter(title__startswith='icecream')` (search for items start with `icecream`)
- `endswith` : `items.filter(title__endswith='icecream')` (search for items end with `icecream`)

## 📑 Filtering 
#### 1. after we fetch the items.
```python
items = MenuItem.objects.select_related('category').all()
```
#### 2. retrive the `category` and `price` query parameters.
```python
category_name = request.query_params.get('category')
to_price = request.query_params.get('to_price')
```
#### 3. check if the api user supplied some value to these parameters
```python
# before the serializers 
if category_name:
    items = items.filter(category__title= category_name)
if to_price:
    items = items.filter(price__lte=to_price)
```

## 📑 Searching
#### 1. as in filtering
#### 2. retrive `search` query parameter. `search = request.query_params.get('search')`
#### 3. apply search logic
```python
if search:
    items = items.filter(title__startwith=search)
```

## 📑Notes
- 💡we use two underscores `__` in filtering process.
- 💡`category__title` represent title field into category model. which mean `category.title`.
- 💡for case-insensitve, we use `i`. `filter(title__iStartwith=search)`