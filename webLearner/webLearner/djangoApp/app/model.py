from django.db import models

#Create your models here.
class PasswordPool(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    #models.IntergerField you can models.InterField() (for the intergers in score section)

    def __str__(self):
        return self.username

#every time we add a model we must migrate so we do, python manage.py makemigrations then python manage.py migrate
'''
#homework of 2022/10/03:

#we create table(another passpool but its a mathtestscore pool)
#check phone photos.

'''

class Homework2(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True)
    studentName=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    score=models.IntegerField()
    def __str__(self):
        return self.studentName
    
class SimpleBlog(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True)
    title=models.CharField(max_length=20)
    content=models.CharField(max_length=200)

class FinalGrade(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    finalgrade=models.IntegerField()
    def __str__(self):
        return self.name
