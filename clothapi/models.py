from django.db import models

class clothes(models.Model):
    name=models.CharField(max_length=120)
    brand=models.CharField(max_length=120)
    material=models.CharField(max_length=120)
    size=models.CharField(max_length=120)
    price=models.PositiveIntegerField()
