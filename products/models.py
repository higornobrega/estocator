from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    bar_code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name + " - Bar code: " + str(self.bar_code)
