from multiprocessing.sharedctypes import Value
from django.db import models

# Create your models here.

class Experience(models.Model):
    nom = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, blank=True)