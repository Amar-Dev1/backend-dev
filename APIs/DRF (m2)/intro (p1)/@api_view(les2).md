# 📑API view decorator ( `@api_view()` )
- 💡 its a decorator that allows you to define a view function that returns a response to an API request.

## 🚀 Benefits of `api_view` function
- 📈 allows you to define a view function that returns a `response` to an API request
- 📊 provides a way to handle API requests and return responses in a structured way
- 📝helps to keep your code organized and maintainable

## api_view response 🆚 normal django response
- 📝 `@api_view` returns a response that is a dictionary with a specific structure
- 📊 normal django response is a HttpResponse object


##  how to use `api_view` function
1. import `api_view` function from `rest_framework.decorators`
2. use `@api_view()` decorator on a view function
3. define the view function to return a response

## Example of api_view function 
```python 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view()
def books(request):
    return Response("list of books",status=status.HTTP_200_OK)
```

## passing HTTP methods to `api_view` 
- `methods`: a list of HTTP methods that the view function allow and will accept it.
- at least pass one http `methon` to `@api_view` => `@api_view(['GET'])` 