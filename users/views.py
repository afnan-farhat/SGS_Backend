from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json

from .models import UserProject, Request
from .serializers import ProjectSerializer, RequestSerializer


# عرض قائمة المشاريع (API)
class ProjectList(APIView):
    def get(self, request):
        projects = UserProject.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


# عرض قائمة الطلبات (API)
@api_view(['GET'])
def request_list(request):
    requests = Request.objects.all()
    serializer = RequestSerializer(requests, many=True)
    return Response(serializer.data)


# إنشاء طلب جديد عبر API POST
@api_view(['POST'])
def create_new_request(request):
    serializer = RequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# طريقة بديلة (غير REST) لإنشاء طلب من POST عادي (مثال)
def insert_request(request):
    if request.method == 'POST':
        Request.objects.create(
            Project_Title=request.POST.get('Project_Title', 'Untitled Project'),
            requestType=request.POST.get('requestType', 'General'),
            Driver=request.POST.get('Driver', 'N/A'),
            Objective=request.POST.get('Objective', 'No Objective'),
            Requirments=request.POST.get('Requirments', 'None'),
            Scope=request.POST.get('Scope', 'General Scope'),
            dep_ID=request.POST.get('dep_ID', 1),
        )
        return redirect('success_page')
    return render(request, 'new-project.html')


def success_page(request):
    return render(request, 'success.html')
# users/views.py
from rest_framework.generics import CreateAPIView
from .models import Request
from .serializers import RequestSerializer

class RequestCreateAPIView(CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    
def post(self, request, *args, **kwargs):
    print("Received data:", request.data)
    return super().post(request, *args, **kwargs)