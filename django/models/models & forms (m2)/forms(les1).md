# 📑 Django Forms

## 💡 What are Django Forms?
- Forms are used to **collect data** from users through **HTML input fields**.
- The data is submitted using the **POST** method.
- Once the user **submits the form**, Django **validates** the data and processes it.

---

## 📑 Form Class

### 💡 What is a Form Class?
- Django provides a **built-in form class** to create forms.
- You can define a **form class** and add fields to it.

### 📘 Example
```python
from django import forms

class CustomForm(forms.Form):
    first_name = forms.CharField(label='Your Name', max_length=100)
```

# 💡 How Does It Work?
- Each field in the form class corresponds to an input field in HTML.

## Example
```python 
first_name = forms.CharField(max_length=100)
```
🔁 converted to : 

```html
<label for="first_name">Your Name</label>
<input type="text" name="first_name" maxlength="100">

```

### 🟢 Notice how the form field in Django is automatically converted to an HTML input field.