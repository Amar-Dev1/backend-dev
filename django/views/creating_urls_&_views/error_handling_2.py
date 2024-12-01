# ❌ in case the client write wrong url , the page must be 404
# 💡 we can create custom view for error page. steps to make this :->

# (myproject)
# - switch DEBUG MODE to FALSE in settings.py

# - add some values to ALLOWED _HOSTS, for ex : ['*'] in settings.py

# - create another urlpattern for error handlers in urls.py and assign it the variable:
handler404 = "myproject.views.handler404"


# - inside views.py create the handler view :
def handler404(request):
    return render("404 : page not found !")


# 📑HttpResponseNotFound
# 💡 its a class and we can use it to return 404 status code with custom message


# 📑 HttpResponse VS HttpResponseNotFound (in error handling)
# HttpResponse is a class return the defualt error message
# HttpResponseNotFound is a class return the 404 page internally, and we can custom the message

# 📑last point
# HttpResponseNotFound is defiend in django.http module
