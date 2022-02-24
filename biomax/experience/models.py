from multiprocessing.sharedctypes import Value
from tkinter.tix import Tree
from tokenize import blank_re
from django.db import models
from ckeditor.fields import RichTextField
import datetime

# Create your models here.


class Experience(models.Model):
    poste = models.CharField(max_length=200)
    body = RichTextField(blank = True, null = True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    start = models.DateField(blank=True, default=datetime.date.today)
    end = models.DateField(blank=True, default=datetime.date.today)

    def __str__(self) -> str:
        return self.poste
    
    def missions(self, Missions):
        self.missions = Missions.objects.select_related().filter(Experience = self)

class Mission(models.Model):
    titre = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    Experience = models.ForeignKey(Experience, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titre

class skills(models.Model):
    titre = models.CharField(max_length=70)
    
