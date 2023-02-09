from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import  get_object_or_404, render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" %username)


def about(request):
    return HttpResponse("About");



def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)
                        
def tasks(request,title):
    task= Task.objects.get(title=title)
    return HttpResponse("Tasks: %s" % task.id)

