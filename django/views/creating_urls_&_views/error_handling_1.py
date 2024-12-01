# dj handle all types of errors by  ⭕ raising exceptins ⭕

# dj raise exception via ⭕ error handling views ⭕

# 📑error handling views :->
# its a views funtions located in seperated file for error handling in views.py (project-level)


# 📑 handling variables :->
# 1. handler400 = 'my_project.views.handler400' (by defualt)
# 2. handler403 = 'my_project.views.handler403' (by defualt)
# 3. handler404 = 'my_project.views.handler404' (by defualt)
# 4. handler500 = 'my_project.views.handler500' (by defualt)

# 💡we can custom the values it

# 📑 Exapmle of error handling views :->


# handler400
# this view will be called when 400 error occurs
def handler400(request, exception):
    return httpResponse("400 :  url error !")


# handler403
# this view will be called when 403 error occurs
def handler403(request, exception):
    return httpResponse("403 :  permission denied !")


# handler404
# this view will be called when 404 error occurs
def handler404(request, exception):
    return httpResponse("404 : page not found ! ")


# handler500
# this view will be called when 500 error occurs
def handler500(request):
    return httpResponse("500 :  internal server error !")
