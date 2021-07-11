from django.db import models

# Create your models here.


class dog(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')


class menudog(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
