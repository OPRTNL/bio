from multiprocessing.sharedctypes import Value
from tkinter.tix import Tree
from tokenize import blank_re
from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.

class Experience(models.Model):
    nom = models.CharField(max_length=200)
    body = RichTextField(blank = True, null = True)
    created = models.DateTimeField(auto_now_add=True, blank=True)