from django.db import models

# Create your models here.

class Order(models.Model):

    objects = None
    name = models.CharField(max_length=23)
    phone = models.CharField(max_length=22)
    address = models.CharField(max_length=23)
    age = models.IntegerField()

    def __str__(self):
        return self.name
