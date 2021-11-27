from django.db import models

class UsrInsert(models.Model):
    UserName=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    class Meta:
        db_table="login"

class UsrRegister(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    class Meta:
        db_table="register"

