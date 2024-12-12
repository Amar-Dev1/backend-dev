# 📑Forms fields and data types
"""
🚀 1. What is a Form in Django?
A Django form is a Python class that defines fields (like input boxes, checkboxes, etc.) to collect user input. It helps with:

- Rendering HTML input elements (like text boxes, dropdowns, checkboxes, etc.)
- Data validation (ensuring the input is correct, like checking if an email is valid)
- Cleaning data (converting the input to the proper data type, like converting "10" to an integer)

"""
# ⚙️ 3. Common Data Types for Form Fields:->
# 📑Check the imgae of data types used in form fields


# 📑widget attribute:->
"""
A widget is a class that renders a form field as an HTML element. Every Django field (like CharField, EmailField, etc.) has a default widget, but you can customize it to:

- Change how the input looks (like adding CSS classes)
- Set attributes (like placeholder, size, maxlength, etc.)
- Change the input type (like from text to password)


for example :->
 name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Adds a Bootstrap class
            'placeholder': 'Enter your name',  # Adds placeholder text
            'style': 'border: 2px solid red;',  # Custom inline styles
        })
    )
"""
