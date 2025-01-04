# 📑API Throttling
### 💡 it`s a technique used to limit the number of requests that can be made to an API within a certain time period. This can help prevent abuse and ensure that the API remains

## 📑Throttling types
### 1️⃣ Anonymous Throttling (Unuthenticated users)
### 2️⃣ User Throttling (Authenticated users)

## 📑How to set up Throttling
- ### Anonymous Throttling
1. create view for it
```python
#views.py

@api_view()
def anon_throttle(request):
    return Response({"message":"successful"})

# urls.py
path('anon-throttle',views.anon_throttle),    
```
2. import `AnonRateThrottle` class and `throttle_classes` decorator
```python
from rest_framework.decorators import throttle_classes
from rest_framework.throttling import AnonRateThrottle
```
3. add `throttle_classes` decorator and pass `AnonRateThrottle` inside it
```python
@api_view()
@throttle_classes([AnonRateThrottle])
def anon_throttle(request):
    return Response({"message":"successful"})

```
4. set the rate limit in `settings.py`
- in `REST_FRAMEWORK` add new section called `DEFAULT_THROTTLE_RATES`
```python
'DEFAULT_THROTTLE_RATES':{
    'anon': '10/minute', # 10 requests per minute
}
```

- ## User Throttling
the key defferent between it and `anonymous` is :
1. import `UserRateThrottle` rather than `AnonRateThrottle`
2. in rate limit, the key will be `user` rather than 'anon'


## 📑 Custom throttling
- 💡say you wanna create throttle for specefic endpoint for users
1. create file called `throttles.py` and the following code :
```python
from rest_framework.throttling import UserRateThrottle

class TenCallsPerMinute(UserRateThrottle):
    scope = 'ten'

# we can use this scope in settings.py file    
```
2. pass this scope in `settings.py`
```python
'ten':'10/minute'
```