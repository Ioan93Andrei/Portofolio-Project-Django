from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def home(request):
  projects = Project.objects.all()
  return render(request, 'portofolio/home.html', {"projects":projects})
