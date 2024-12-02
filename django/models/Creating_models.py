# 📑Creating Models :->

# 📑Introduction example :->
"""
Class Menu(models.Model):

    these are the columns 👇 :      

    name = models.CharField(max_lenght = 100)
    cuisine = models.CharField(max_lenght = 100)
    price = models.IntegerField()

"""

# 📑Handle with models in Dj :->

# 💡 first : I need to make migrations :
"""
1. add the model inside settings.py (project-level) : 
    INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    ...
    ]
2. ` manage.py makemigrations` (migration file initialized ✅)
3. `python manage.py migrate`
"""
# 💡second : To access the model using query and add data :
"""
1. satrt python shell : `python manage.py shell`
2. import the model : `from myapp.models import Menu`
3. Create data : 
                n = Menu.objects.create(name='pasta',cuisine='italian',price=10)
4. Update data : 
                p = Menu.objects.get(pk=2)
                p.price = 20
                save()
5. Retrive data :
                Menu.objects.all()

"""
