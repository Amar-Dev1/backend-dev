# 📑class based views

# 💡 it`s an another way to write views using OOP
# 💡 allows u to use views like objects
# 💡 views is callable and use classes instance, which is not found in function based views

# class based view VS function based view :->

def function_view(request):
    if request.method == "GET":
        # view logic
        return HttpResponse("")


class class_view:
    def get(self, request):
        # view logic
        return HttpResponse("")


# 📑Mixins
# 💡 it`s a class that contains a set of methods that can be used in other classes

# 📑 some common mixins developer use :->
# Create
# List
# Retrieve
# Update
# Delete
# 💡 it`s a good practice to use mixin to avoid code duplication
