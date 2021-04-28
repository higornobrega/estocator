from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.name
