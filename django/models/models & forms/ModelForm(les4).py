# 📑ModelForm:->
# 💡it`s built-in django class for combining Model and Form classes.
# 💡by use it , we can collect the data from the form and store it into the database.

# 📑Steps:->

# 1️⃣ after define the model , Import the it to use it in ModelForm in (forms.py).
"""
from .models import inputModel (the model)
"""

# 2️⃣ Create a new class that inherits from ModelForm in (forms.py).
"""
class inputModelForm(forms.ModelForm):
    class Meta:
        model = inputModel
        fields = '__all__' (to select all fields)

"""

# 3️⃣Create a view to this ModelForm:->
"""
i can add some code to make simple process:->

form = inputModelForm()
if request.method == 'POST':

    form = inputModelForm(request.POST)
context= {"form" : form}
return render(request, "form.html", context)

"""

# ❗ Notes :-> 
"""
1. make sure that you register the model in admin.py ❗
2. make sure that you implement the migrations ❗

"""