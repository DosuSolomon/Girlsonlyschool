from django.db import models

# Create your models here.

class School_info(models.Model):

    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    link = models.CharField(max_length=500)

class Contact():
    name = str
    phone_no = int

class Latest_Post(models.Model):

    img = models.ImageField(upload_to='pics')
    post = models.TextField()
    date = models.DateField()
    name = models.CharField(max_length=100)
