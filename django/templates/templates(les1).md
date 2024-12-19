# 📑Templates

💡It’s a text file (HTML file) used in Django projects. Templates represent the `presentation layer` in the (3-tier architecture).

## 📑To make templates run:->

💡In the `TEMPLATES` list, add the `templates` value to the `DIRS` in `Settings.py`.

## 📑Dynamic HTML content :

💡We can use Django Template Language (DTL) or Jinja2 to create dynamic HTML content.
💡DTL is a templating engine that allows us to insert Python code into our HTML.
💡We can use DTL to display data from our models in our templates.

## 📑Variable tag:

💡We can use the `{{ }}` syntax to display variables in our templates. 
For example: `{{ user.name }}` will display the user's name.

## 📑Logic tag 

💡We can use the `{% %}` syntax to perform logic in our templates. 
For example: `{% for user in users %}` will loop through all users.
💡The logic tag should have a closing tag, like `{% endfor %}` for `{% for user in users %}`.

## 📑Filters

💡Filters are used to format data in our templates.
💡We can use filters to format dates, numbers, and strings. The syntax is: `{{ variable_name | filter_name }}`
  
### 📑Examples for filters:->

- **Upper filter:** `{{ name | upper }}` → Transforms the name to uppercase.
- **Lower filter:** `{{ name | lower }}` → Transforms the name to lowercase.
- **Length filter:** `{{ nums | length }}` → Shows the length of the `nums` list.
- **Wordcount filter:** `{{ title | wordcount }}` → Counts the number of words in the title string.
- **Slice filter:** `{{ nums | slice:"1:3" }}` → Creates a slice of the `nums` array from index 1 to index 3.

## 📑Template inheritance

💡We can use template inheritance to create a base template that other templates can inherit from.
💡We use the `{% extends %}` tag to specify the base template.

# 📑Notes

💡The `render` function accepts 3 arguments:
1. Request object
2. Template name
3. Dictionary of variables to pass to the template
