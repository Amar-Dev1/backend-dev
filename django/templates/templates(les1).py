# 📑Template:->
"""
💡it`s a text file (html file) for the django project.
💡templates represent a `presentation layer` in the (3 tire architecture).
"""

# 📑To make templates run :->
# 💡add the template to the templates list in `Settings.py`.

# 📑Dynamic html content:->
"""
💡we can use django template language (DTL) or jinja2 to create dynamic html content
💡DTL is a templating engine that allows us to insert python code into our html
💡we can use DTL to display data from our models in our templates
"""

# 📑Varible tag:->
"""
💡we can use the `{{ }}` syntax to display variables in our templates. like {{ user.name }}
"""

# Logic tag:->
"""
💡we can use the `{% %}` syntax to perform logic in our templates. like {{% for user in users %}}.
💡the logic tag should have a closing tag . like {{% endfor %}} for {{% for user in users %}}.
"""

# 📑Filters:->
"""
💡filters are used to format data in our templates
💡we can use filters to format dates, numbers, and strings . like {{ variable_name | filter_name }} 
"""

# 📑Examples for filters:->
"""
💡upper filter: {{ name | upper }} => name with upper format
💡lower filter: {{ name | lower }} => name with lower format
💡lenght filter: {{ nums | lenght }} => length of the nums
💡wordcount filter: {{ title | wordcount  }} => number of words in the string
💡slice filter: {{ nums | slice[1:3]  }} => make slice on the nums
"""

# 📑Template inheritance:->
"""
💡we can use template inheritance to create a base template that other templates can inherit from
💡we can use the `{% extends %}` tag to specify the base template
"""

# 📑Note:->
"""
💡render function accept 3 arguments:->
1. request object
2. template name
3. dictionary of variables to pass to the template
"""
