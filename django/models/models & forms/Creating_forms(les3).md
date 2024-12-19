# 📑 Creating Forms in Django

---

## 💡 Key Concepts:
- Every form field in Django is **required by default**, meaning it must be filled out by the user.
- You can make a field optional by setting **`required=False`**.

---

## 🔥 Steps to Create a Form

### 1️⃣ **Define the Form Class `forms.py`**
This is where you define the **fields** for the form. Each field represents an input in the HTML form.

```python
from django import forms

class UserInput(forms.Form):
    name = forms.CharField(max_length=100)  # Text input
    email = forms.EmailField()  # Email input
    password = forms.CharField(widget=forms.PasswordInput)  # Password input
```
    
### 2️⃣ **Create a view for the form in `views.py`**
```python 
from django.shortcuts import render
from .forms import UserInput  # Import the form

def form_view(request):
    form = UserInput()
    context = {"form": form}
    return render(request, "form.html", context)

```

### 3️⃣ **Create the Template for the Form `form.html`**
```python
<form action="" method="POST">
    {% csrf_token %}
    {{ form }} <!-- Automatically renders all form fields -->
    <input type="submit" value="Submit">
</form>
```

### 🔥 **Final Touch: Add the Form App to `settings.py`**
```python 
INSTALLED_APPS = [
    ...
    'your_app_name',  # Add the name of your app here
]

```