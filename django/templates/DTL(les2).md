# 📑DTL

- 💡Stands for `Django Template Language`. It comes with Django and is used to render dynamic content.
- 💡It’s based on Jinja2.

# 📑Main Constructs of DTL:->

## 1️⃣Variables: `{{ variable_name }}`
- A variable returns a dictionary-like object.

## 2️⃣Tags: `{% tag_name %} {% endtag %}`
- Tags are used to perform actions like looping, conditional statements, etc.

## 3️⃣Filters: `{ variable | filter }`
- Consists of 2 arguments separated by a pipe (|): variable and filter.
- Filters are used to perform operations on a variable, like string formatting, date formatting, etc.

## 4️⃣Comments: `{% comment "this is comment" %} {% endcomment %}`
- Comments are used to add comments in the template.
