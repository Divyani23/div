from django.db import models

# Create your models here.
class StudentData(models.Model):
    Question=models.CharField(max_length=300)
    Teacher=models.CharField(max_length=50)
    QuestionBank=models.CharField(max_length=1000)
