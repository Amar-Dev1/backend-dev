# 📑Data Sanitization
- 💡Sanitization is the process of cleaning data from potential threats
- 💡Without proper sanitization, your API can be exploited using common attacks like **SQL injection**
- 💡Client applications can suffer attacks like **cross-site** scripting or session hijacking via **injecting JavaScript**

## 🔵 Sanitize HTML and JavaScript 
- hackers can use `<script>` tags to inject JavaScript and `<img>` tags to add unwanted trackers.

## 🤔 How to beat them ❓
### we can use third-party liberary called `bleach`
step one : install `bleach` package
```python
pipenv install bleach
```
step tow : import the `bleach` module in the `serializers.py` file. 
```python 
import bleach
```
step three : Sanitize the field data using both the validate_field() and validate() methods
```python
def validate_title(self, value):
        return bleach.clean(value)
```