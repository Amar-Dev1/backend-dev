# 📑Templates Inheritance 

- 💡The child can add new content in addition to the parent content.
- 💡To apply template inheritance, there are two main tags:->

## 1️⃣extends: 
Used to inherit content from the parent to the child. For example, (extend content from the base to the about page). 
   - Ex: `{% extends "base.html" %}`

## 2️⃣include:
Used to include some content in an HTML page, like including the header component in the base file.
   - Example : `{% include "header.html" %}`
