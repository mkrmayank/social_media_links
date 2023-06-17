# from datetime import date, datetime
from django.db import models

# Create your models here.

class Register(models.Model):
    img = models.ImageField(upload_to = "media/", default="")
    name = models.CharField(max_length=122, default="")
    number = models.CharField(max_length=12)
    designation = models.TextField()
    about = models.TextField(max_length=150, default="")
    social1 = models.CharField(max_length=122, default="")
    social2 = models.CharField(max_length=122, default="")
    social3 = models.CharField(max_length=122, default="")
    social4 = models.CharField(max_length=122, default="")
    social5 = models.CharField(max_length=122, default="")


    def __str__(self):
        return self.name
