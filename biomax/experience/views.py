from django.shortcuts import render
from django.http import request
from .models import Experience, Mission

# Create your views here.

def index(request):
    experiences = Experience.objects.all()
    experience_missions = []
    for experience in experiences:
        missions = Mission.objects.select_related().filter(Experience = experience)
        experience_missions.append({'experience' : experience, 'missions' : missions})
    print(experience_missions)
    return render(request,'experience/index.html',{'experience_missions' : experience_missions})
