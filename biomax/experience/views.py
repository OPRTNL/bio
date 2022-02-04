from django.shortcuts import render
from django.http import request
from .models import Experience, Mission

# Create your views here.

def index(request):
    experiences = Experience.objects.all()
    for experience in experiences:
        experience.missions(Mission)
        print(experience)
    return render(request,'experience/index.html',{'experiences' : experiences})
