from django.db import models

# Create your models here.


class Phones(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price = models.PositiveIntegerField()