# 📑Django Forms

# 💡we collect data from user using forms with ⭕POST⭕ method, once user submit the form ✅.


# 📑Form Class:->
# 💡using form class (built-in Dj) , we can define form class and add our fields. Ex:->
"""
class Form(forms.Form):
    first_name = forms.CharField(label='Your Name',max_lenght=100)
"""

# 💡Note :->
"""
every field in the form class represent input field in HTML . for example :->
1️⃣ first_name = forms.CharField(ma_lenght=100)
2️⃣ <label name="Your Name"> <input type="text" max_lenght=100 name="first_name">

1️⃣ === 2️⃣

"""
