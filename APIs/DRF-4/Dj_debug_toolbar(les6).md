# 📑 Django debug toolbar 
- 💡 its a dj debugger appear only in development environment. 
- 💡 useful for debug dj project and optimize it.
- 💡 it can be installed by pip install django-debug-toolbar


## 🔁 install django debug toolbar (using pipenv)
- 💡 after activating the virtual environment : 
1. install it : `pipenv install django-debug-toolbar`
2. add it to `INSTALLED_APPs` : `debug-toolbar`
3. add url to it : `path('__debug__/',include('debug_toolbar.urls'))`
4. add it to `MIDDLEWARE` : `debug_toolbar.middleware.DebugToolbarMiddleware`
5. add new section called `INTERNAL_IPS` : 
```python  
INTERNAL_IPS = [
    '127.0.0.1',
]
```

## 📑 Django debug toolbar sections
- 💡 I can hide it 
- 💡 it has several sections :
1. **Request**: shows the request details.
2. **Templates**: shows the templates used in the request.
3. **SQL**: shows the SQL queries executed in the request.
4. **Settings**: shows the project settings.
7. **Cache**: shows the cache details.