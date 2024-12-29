# 📑 Types of Relationships

1. One to One
2. One to Many
3. Many to Many

# 📑 One to One Relationship

- 💡 One record in a table is related to exactly one record in another table.
- 💡 We implement it using `OneToOneField`.

```python

class College(models.Model):
    CollegeID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    website = models.URLField()

class Teacher(models.Model):
    CollegeID = models.OneToOneField(  # Relationship here
        College,
        on_delete=models.CASCADE
    )
    Qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
```
# 📑 One to Many Relationship

- 💡 One record in a table is related to many records in another table.
- 💡 We implement it using `ForeignKey`.
```python
class Subject(models.Model):
    Subjectcode = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    credits = models.IntegerField()

class Teacher(models.Model):
    TeacherID = models.IntegerField(primary_key=True)
    subjectcode = models.ForeignKey(  # Relationship here
        Subject,
        on_delete=models.CASCADE
    )
    Qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

```

# 📑 Notes
- 💡 on_delete: Option specifies the behavior when the associated object in the primary model is deleted.

- `CASCADE`: Deletes the object containing the `ForeignKey`.
- `PROTECT`: Prevents deletion of the referenced object.
- `RESTRICT`: Prevents deletion of the referenced object by raising `RestrictedError`.


# 📑 Many to Many Relationship
- 💡 Many records in a table are related to many records in another table.
- 💡 We implement it using `ManyToManyField`.
```python
class Teacher(models.Model):
    TeacherID = models.IntegerField(primary_key=True)
    Qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

class Subject(models.Model):
    Subjectcode = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    credits = models.IntegerField()
    teacher = models.ManyToManyField(Teacher)  # Relationship here

```