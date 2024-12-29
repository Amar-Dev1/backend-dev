# 📑Class-based views
- 💡 write less code
- 💡 less code duplication
- 💡 extend and add features
- 💡 methods for HTTP request types

## using Class-based view
1. import `APIView` from `rest_framework.views`.
2. Create a class that inherits from `APIView`.
3. Define methods for each HTTP request type (e.g., `get`, `post`,`put`)
4. map the 

## Example of Class-based view
```python
## views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookList(APIView):
    def get(self,request):
        return Response({"message":"List of books 📑",status=status.HTTP_200_OK})
    def post(self,request):
        return Response({"message":"New book created ✅",status=status.HTTP_200_OK})

# urls.py (project)
urlpatterns = [
   ...
    path('books/',views.BookList.as_view()),
    ...
]

```
## Get the books by author
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookList(APIView):
    def get(self,request,author):
        author = request.GET.get('author')
        if (author):
            return Response({"message":"List of books by"+author},status=status.HTTP_200_OK)
        return Response({"message":"List of books 📑",status=status.HTTP_200_OK})  
```

##