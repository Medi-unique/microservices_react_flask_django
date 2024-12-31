from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    likes=models.IntegerField(default=0)
class User(models.Model):
    pass
    # name=models.CharField(max_length=200)
    # email=models.CharField(max_length=200)
    # password=models.CharField(max_length=200)
    # likes=models.ManyToManyField(Product)
