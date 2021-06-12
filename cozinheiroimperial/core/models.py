from django.db import models


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=60)
    directions = models.CharField(max_length=400)
