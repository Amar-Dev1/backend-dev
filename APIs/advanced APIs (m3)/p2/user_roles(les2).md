# User roles
to ensure the api is secure and request come from the right users, we have to check the user roles (authorization)

## How to implement ?
1. create user from admin panel (for example) and assign it to a group
2. create a view for this group and check if the user in this group or not
3. if the user is in the group, then the view will be rendered

```python
# views.py

@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name="Manager").exists():
        return Response({"message": "Only managers can see this ✅"})
    else:
        return Response({"message": "you are not authorized ❌"}, 403)  

# urls.py  
path('api-token-auth/',obtain_auth_token),
path('manager',views.manager_view),
```