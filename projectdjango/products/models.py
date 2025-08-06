from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def is_in_stock(self):
        return self.stock > 0