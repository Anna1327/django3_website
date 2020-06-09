from django.db import models

# Create your models here.

class Products(models.Model):
    id = models.AutoField(primary_key=True)

    category = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads')
    color = models.CharField(max_length=10, blank=True, null=True)
    brand = models.CharField(max_length=30, blank=True, null=True)
    size = models.CharField(max_length=5, blank=True, null=True)
    tags = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    price_sale = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.category} - {self.name}'