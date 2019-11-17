from django.db import models


# Create your models here.
class AnotherModel(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
