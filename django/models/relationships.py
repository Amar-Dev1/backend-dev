# 📑Type of relationships

# 1. one to one
# 2. one to many
# 3. many to many


# 📑one to one :->

"""
💡one record in a table is related to exactly one record in another table
💡we implement it using OneToOneField
    class college(Model): 
    CollegeID = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=50) 
    strength = models.IntegerField() 
    website=models.URLField() 

    class Teacher(models.Model): 
    CollegeID = models.OneToOneField(            👈 relationship here
                College, 
                on_delete=models.CASCADE 
                ) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50) 
"""

# 📑one to many :-
"""
💡one record in a table is related to many records in another table
💡we implement it using ForeignKey
    class Subject(models.Model): 
        Subjectcode = models.IntegerField(primary_key = True) 
        name = models.CharField(max_length=30) 
        credits = model.IntegerField() 

    class Teacher(models.Model): 
        TeacherID = models.ItegerField(primary_key=True) 
        subjectcode=models.ForeignKey(                        👈 relationship here
                    Subject,  
                    on_delete=models.CASCADE 
                    ) 
        Qualification = models.CharField(max_length=50) 
        email = models.EmailField(max_length=50) 
"""

# 📑Notes :->
"""
💡on_delete: option specifies the behavior in case the associated object in the primary model is deleted
💡CASCADE: deletes the object containing the ForeignKey
💡PROTECT: Prevent deletion of the referenced object.
💡RESTRICT: Prevent deletion of the referenced object by raising RestrictedError
"""

# 📑many to many :->
"""
💡many records in a table are related to many records in another table
💡we implement it using ManyToManyField

    class Teacher(models.Model): 
        TeacherID = models.ItegerField(primary_key=True) 
        Qualification = models.CharField(max_length=50) 
        email = models.EmailField(max_length=50) 

    class Subject(models.Model): 
        Subjectcode = models.IntegerField(primary_key = True) 
        name = models.CharField(max_length=30) 
        credits = model.IntegerField() 
        teacher = model.ManyToManyField(Teacher)         👈 relationship here
"""
