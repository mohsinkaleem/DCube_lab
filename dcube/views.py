from django.urls import reverse
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Projects
# from django.contrib import messages

def projects_list(request):
    projects = Projects.objects.all()
    return render(request,"dcube/projects.html",context={'projects':projects})

def each_project(request,pk):
    project=get_object_or_404(Projects, pk=pk)
    return render(request,'dcube/blog-details.html',context={"project":project})


