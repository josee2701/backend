# models.py
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name} {self.apellido}"