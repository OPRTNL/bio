from django.db import models

# Create your models here.

class Experience(models.Model):
    nom = models.CharField(max_length=200)