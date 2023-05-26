from django.db import models
class UserDB(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True)
    username=models.CharField(max_length=20)
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