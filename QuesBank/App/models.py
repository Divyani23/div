from django.db import models

# Create your models here.
class Data(models.Model):
    Questions=models.CharField(max_length=250)
    Teacher Name=models.CharField(max_length=30)
    Question Bank=models.CharField(max_length=3000)
