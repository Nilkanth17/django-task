from django.db import models 
from django.db.models import Model
from datetime import datetime
from rest_framework import serializers
# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):  
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class item(models.Model):
    name = models.CharField(max_length=100)
    price =  models.IntegerField()
    description = models.CharField(max_length=225)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.now())
    image = models.FileField(upload_to="media/", default="default.jpg")
        
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    city = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name


class login_ragister(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

