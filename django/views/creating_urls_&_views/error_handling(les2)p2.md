# 📑 **Custom 404 Error Page in Django**

When a client accesses an incorrect or non-existent URL, Django responds with a **404 Page Not Found** error. Instead of using the default Django error page, you can create a **custom 404 error page**.

---

## 🚀 **Steps to Create a Custom 404 Error Page**
1. **Switch DEBUG Mode to False**  
   - Open `settings.py` and set:  
     ```python
     DEBUG = False
     ```

2. **Update Allowed Hosts**  
   - Add allowed hosts in `settings.py`:  
     ```python
     ALLOWED_HOSTS = ['*']  # Use '*' for all hosts, or specify specific domains
     ```

3. **Set Custom 404 Handler in urls.py**  
   - Add the following line in `urls.py`:  
     ```python
     handler404 = 'myproject.views.handler404'
     ```

4. **Create Custom 404 View in views.py**  
   - Define a custom view for handling 404 errors:  
     ```python
     from django.shortcuts import render

     def handler404(request, exception=None):
         return render(request, '404.html', status=404)
     ```

   > 📝 **Note:** Make sure to create a `404.html` file in your templates directory. This is the HTML file that will be displayed when the error occurs.

---

## 📚 **HttpResponseNotFound**

**HttpResponseNotFound** is a special class in Django used to return a **404 status code** along with a custom message.  

### 🔹 **Usage Example**
```python
from django.http import HttpResponseNotFound

def custom_404_view(request):
    return HttpResponseNotFound("404: Page Not Found!")
```

## 📑 **HttpResponse vs. HttpResponseNotFound**

| **Class**              | **Purpose**                      | **Response**                     |
|-----------------------|-----------------------------------|-----------------------------------|
| **HttpResponse**       | General-purpose response class   | Returns a standard HTML response |
| **HttpResponseNotFound** | Used specifically for 404 errors | Returns a 404 status response    |
