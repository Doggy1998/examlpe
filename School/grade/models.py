from django.db import models

# Create your models here.
class Grade(models.Model):
    student = models.CharField(max_length=50)
    subject = models.CharField(max_length=30)
    score = models.IntegerField(default=0)