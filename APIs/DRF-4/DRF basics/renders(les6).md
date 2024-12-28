# 📑 Renderers

## 💡 What are Renderers?  
Renderers are responsible for determining how the output of your **APIs** is formatted and displayed to the client. The output can be in various formats, such as `JSON`, `XML`, `HTML`, etc.

---

## Types of Renderers  

### 1️⃣ Built-in Renderers  
The Django REST Framework (DRF) provides several built-in renderers:  
- **JSONRenderer**: Outputs data in JSON format (default).  
- **XMLRenderer**: Outputs data in XML format.  
- **BrowsableAPIRenderer**: Provides an interactive HTML interface for browsing APIs.

### 2️⃣ Third-party Renderers  
For additional functionality, you can use third-party renderers:  
- **XMLRenderer**: Advanced XML rendering support.  
- **YAMLRenderer**: Outputs data in YAML format.  
- **JSONPRenderer**: Adds support for JSONP (JSON with Padding).

---

## 💡 Default Renderers in DRF  
By default, DRF uses the following renderers:  
1. **JSONRenderer**  
2. **BrowsableAPIRenderer**

---

## 💡 How to Change the Default Renderer?  

1. Open the `settings.py` file of your Django project.  
2. Add or update an object called `REST_FRAMEWORK`.  
3. Specify the desired renderer classes under the `DEFAULT_RENDERER_CLASSES` key.  

### Example:
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',          # Use JSON format
        'rest_framework.renderers.BrowsableAPIRenderer',  # Use Browsable API
    ],
}
```
## 💡 Disable the Browsable API
- If you want your API to output only JSON, remove the `BrowsableAPIRenderer`:
```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',  # Only JSON output
    ],
}

```

## 💡 How to Set the Content Type for API Responses ?
Clients can specify the desired output format by setting the `Accept` header in their **HTTP request**.
- To request JSON:
```http
Accept: application/json
```
- To request XML:
```http
Accept: application/xml
```