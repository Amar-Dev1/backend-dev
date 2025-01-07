# 📑 Throttles in Class-based views
- 💡to use throttle in class-based views
1. add the classes to `REST_FRAMEWORK` in `settings.py `
```python
'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
],
```
2. use the throttle classes in your view
- we need to pass the throttle classes to a public class property called throttle_classes
```python
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class MenuItemsViewSet(viewsets.ModelViewSet):
    # here 👇
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # here 👆
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
```
3. add the rate limit in `REST_FRAMEWORK`
```python
'DEFAULT_THROTTLE_RATES': {
        'anon': '2/minute',
        'user': '10/minute'
}
```

## 💡 Conditional throttling
With conditional throttling, we can throttle API endpoints only for the specific HTTP methods, like `GET` calls, or `POST` calls.
```python 
class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
 
    def get_throttles(self):
        if self.action == 'create':
            throttle_classes = [UserRateThrottle]
        else:
            throttle_classes = []  
        return [throttle() for throttle in throttle_classes]
```
#### 💡Notice that `throttle_classes` is not used as a public attribute this time, which means the following line from the previous code example was removed.

## 📑Custom throttling classes
just import the custom throttle class and add it in `throttle_classes`
```python
# views.py

from .throttles import TenCallsPerMinut # 👈 throttle class

throttle_classes = [TenCallsPerMinut]
```