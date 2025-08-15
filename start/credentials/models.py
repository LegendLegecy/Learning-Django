from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField


class Credential(models.Model):
    """
    Model to store credentials for various services.
    """
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255) 


class Product(models.Model):
    """
    Model to store product information.
    """
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = HTMLField()
    image = models.ImageField(upload_to='products/')
    slug = AutoSlugField(populate_from='name',unique=True,null=True,default=None)