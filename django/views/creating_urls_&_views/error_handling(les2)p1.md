# 📑 **Django Error Handling**

Django handles errors by **raising exceptions** and **redirecting them to error-handling views**. These views allow developers to customize the response for specific HTTP error codes.

---

## 🚀 **How Django Handles Errors**
1. **Raising Exceptions**: Django raises specific exceptions for different errors.  
2. **Error-Handling Views**: These are special views used to customize responses for errors.  
3. **Customizable Handlers**: You can customize how errors like 400, 403, 404, and 500 are handled.  

---

## 📑 **Error-Handling Views**
Error-handling views are **custom view functions** that Django calls whenever an error occurs. They are defined at the **project level** (typically in `views.py` or a similar file).

### 🔧 **Default Error Handlers**
By default, Django uses the following view handlers for common errors:  

| **Error Code** | **Handler**                          | **Description**                  |
|-----------------|--------------------------------------|-----------------------------------|
| **400**         | `handler400 = 'my_project.views.handler400'` | **Bad Request** (Invalid URL, form, etc.) |
| **403**         | `handler403 = 'my_project.views.handler403'` | **Permission Denied** (User not authorized) |
| **404**         | `handler404 = 'my_project.views.handler404'` | **Page Not Found** (URL not found) |
| **500**         | `handler500 = 'my_project.views.handler500'` | **Internal Server Error** (Server crash or bug) |

> 💡 **Note:** These handlers are customizable, and you can override them in your `urls.py` file.  

---

## 📚 **Example of Custom Error-Handling Views**

Here’s how you can create custom views for these errors in `views.py`:

### 🔹 **Handler for 400 (Bad Request)**
```python
def handler400(request, exception):
    return HttpResponse("400: URL error!")
```
### 🔹 Handler for 403 (Permission Denied)
```python
def handler403(request, exception):
    return HttpResponse("403: Permission denied!")
```
### 🔹 Handler for 404 (Page Not Found)
```python
def handler404(request, exception):
    return HttpResponse("404: Page not found!")
```

### 🔹 Handler for 500 (Internal Server Error)
```python
def handler500(request):
    return HttpResponse("500: Internal server error!")
```

### 🔧 How to Set Custom Handlers in `urls.py`
```python
handler400 = 'my_project.views.handler400'
handler403 = 'my_project.views.handler403'
handler404 = 'my_project.views.handler404'
handler500 = 'my_project.views.handler500'
```