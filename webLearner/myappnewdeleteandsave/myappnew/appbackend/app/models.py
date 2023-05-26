from django.db import models
class UserDB(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True)
    username=models.CharField(max_length=20)#mark 123
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.username

# Create your models here.
'''
homework:
2022/11/01
1.create database, UserDB table
2.this table must be shown in admin, signup can add user in userDB
3.after signup we can use this username and password to login
4. lenght of username is bigger than 5, password must contain at least a capital letter, lower case letter and lenght of the password must ne more than 8(you can use backend and frontend to do this)
'''
class UserInfo(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True)
    username=models.CharField(max_length=20)#mark 123 cant change, same as userdb
    name=models.CharField(max_length=20)#change some stuff in main page, replace user with name
    nickname=models.CharField(max_length=20)
    occupation=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    hobby=models.CharField(max_length=20)
    def __str__(self):
        return self.username

class BlogInfo(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True)
    title=models.CharField(max_length=200)
    blogdata=models.CharField(max_length=200000)
    timerecord=models.DateTimeField()
    def __str__(self):
        return self.title