
# regular experssion let u make a dynamic urls

# should import re_path form django.urls

form django.urls import path,re_path

urlpatterns=[
     path('menu_item/<int:id>',views.books) # <-- without regexp ❌
     re_path(r'^menu_item/([0-9]{2})/$' ,veiws.display_menu_item) # <--- with regexp ✅
 ]

# 📑 Examples : 

# /menu_item/03 ✅
# /menu_item/123 ❌

# 📑Demonstrate

# r (row string) :->
#  treat the symbols like string characters not escape characters 

# ^ :->
# used as the anchor for the start of string

# $ :->
# used as the anchor for the end of string


# {2} :->
# used to specify the number of characters
