from functools import update_wrapper
from django.db import models

# Create your models here.
#TODO categoris: samsung, noutbuks: acer, macbook, asus, accessories: earphones, powerbank**2  


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(primary_key=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        if self.parent:
            return f'{self.parent} --> {self.title}'
        return self.title

class Product(models.Model):
    STATUS_CHOICES = (
        ('in stock', 'в наличии'),
        ('out of stock', 'нет в наличии'),
        ('awaiting', 'ожидается')
    )

    def __str__(self):
        return self.name

    name = models.CharField(max_length=155)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='prod_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')