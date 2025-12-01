from django.db import models

# Create your models here.


class Register(models.Model):
    Fname=models.CharField(max_length=100)
    Lname=models.CharField(max_length=100)
    Phone=models.CharField(max_length=10)
    Email=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)