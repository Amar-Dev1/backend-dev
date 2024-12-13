# 📑For Creating forms:->

# 💡Note:-> Every Field by default is required, we can change it by the attribute: required = Flase
"""
1️⃣ define form class (forms.py) :->

class UserInput(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.PasswordField()

    
2️⃣ Create a view for the form in (views.py) :->

def form_view():
    form = UserInput()
    context = {"form":form}
    return render(request, "form.html", context)


3️⃣ Create template for the form (form.html):->

<form action= "" method="POST">
{% csrf_token %}
{{ form }}
<input type="submit"value="submit"?
</form>
     
"""

# 💡Note that make sure you defined the app in settings.py file
