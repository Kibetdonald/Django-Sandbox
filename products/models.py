from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=200)
    productprice = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='pics')