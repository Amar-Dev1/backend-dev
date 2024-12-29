# 📑 ModelForm in Django

---

## 💡 Key Concepts:
- **ModelForm** is a built-in Django class that **combines a Model with a Form**.
- It allows you to collect data from a form and **store it directly in the database**.
- Instead of defining form fields manually, ModelForm automatically generates them from the model.

---

## 🔥 Steps to Create a ModelForm

### 1️⃣ **Define the Model `models.py`**
Before creating a ModelForm, you must define the model that represents the database table.

```python
from django.db import models

class InputModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
```

### 2️⃣ Create the ModelForm `forms.py`
The ModelForm automatically generates form fields based on the model's fields/
```python 
from django import forms
from .models import InputModel  # Import the model

class InputModelForm(forms.ModelForm):
    class Meta:
        model = InputModel  # Link the form to the model
        fields = '__all__'  # Use all fields from the model

```

### 3️⃣ Create a View for the ModelForm `views.py`
The view will process and save form data to the database when the form is submitted.
```python 
from django.shortcuts import render
from .forms import InputModelForm  # Import the ModelForm

def form_view(request):
    form = InputModelForm()  # Empty form to display
    if request.method == 'POST':
        form = InputModelForm(request.POST)  # Bind form to POST data
        if form.is_valid():  # Validate form data
            form.save()  # Save form data to the database
    context = {"form": form}
    return render(request, "form.html", context)

```

### 4️⃣ Create the Form Template `form.html`
This is the HTML file where the form will be displayed and submitted.

```python 
<form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}  <!-- Automatically renders all form fields -->
    <input type="submit" value="Submit">
</form>

```

### 5️⃣ Register the Model in `admin.py`
This allows you to view, add, and edit data in the Django admin dashboard.
```python
from django.contrib import admin
from .models import InputModel  # Import the model

admin.site.register(InputModel)

```

### 6️⃣ Run Migrations to Update the Database
apply the changes to the database :
```python
python manage.py makemigrations  # Create the migration files
python manage.py migrate  # Apply the migrations to the database

```


## ⚠️ Important Notes
- Make sure to use `form.save()` in the view to save form data to the database.
- Check for form validation using `form.is_valid()` before saving to avoid bad data.