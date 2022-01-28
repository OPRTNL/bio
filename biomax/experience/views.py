from django.shortcuts import render
from django.http import request
from .models import Experience

# Create your views here.

def index(request):
    experiences = Experience.objects.all()
    return render(request,'experience/index.html',{'experiences' : experiences})
