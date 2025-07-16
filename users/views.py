from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import UserProject

# Create your views here.
# request -> response
# request handler
# action = view in Django 


def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    # Pull data from db
    # Transform 
    # send email
    x = calculate ()
    return render(request,  'hello.html', {'name': 'Afnan'})

def all_users(request):
    return HttpResponse('Returning all user')


# views.py

def project_list(request):
    projects = UserProject.objects.all()  
    return render(request, 'projects_list.html', {'projects': projects})


def new_project(request):
    projects = UserProject.objects.all() 
    return render(request, 'new-project.html', {})


from django.shortcuts import render, redirect
from .models import Request


def insert_request(request):
    if request.method == 'POST':
        Request.objects.create(
            Project_Title=request.POST.get('Project_Title', 'Untitled Project'),
            requestType=request.POST.get('requestType', 'General'),
            Driver=request.POST.get('Driver', 'N/A'),
            Objective=request.POST.get('Objective', 'No Objective'),
            Requirments=request.POST.get('Requirments', 'None'),
            Scope=request.POST.get('Scope', 'General Scope'),
            dep_ID=request.POST.get('dep_ID', 1),  # add if needed
            # request_state auto set to "waiting"
        )
        return redirect('success_page')
    return render(request, 'new-project.html')


def success_page(request):
    return render(request, 'success.html')
