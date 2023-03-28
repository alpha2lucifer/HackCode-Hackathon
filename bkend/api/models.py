from django.db import models

# Create your models here.
class Udata(models.Model):
    Uname = models.CharField(max_length=100)
    email= models.CharField(max_length=100)