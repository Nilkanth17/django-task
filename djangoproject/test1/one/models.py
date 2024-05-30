from django.db import models

# Create your models here.

class Online(models.Model):
  category = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
    

def __str__(self):
    return self.category

