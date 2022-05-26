from django.db import models

# Create your models here.

class relatives(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()