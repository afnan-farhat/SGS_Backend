from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import UserProject, Request, Employee
from .serializers import ProjectSerializer, RequestSerializer, EmployeeSerializer


# عرض قائمة المشاريع (API)
class ProjectList(APIView):
    def get(self, request):
        projects = UserProject.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    

class EmployeeList(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')

    try:
        employee = Employee.objects.get(email=email)
        return Response({
            "success": True,
            "Emp_ID": employee.Emp_ID,
            "Emp_name": employee.Emp_name,
            "Emp_role": employee.Emp_role,
            "job_title": employee.job_title,
            "email": employee.email,
            "chat": employee.chat,
            "work_phone": employee.work_phone,
            "buisness_address": employee.buisness_address,

            
        })
    except Employee.DoesNotExist:
        return Response({"success": False, "error": "Invalid email"}, status=400)

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



def request_detail_api(request, request_id):
    request_instance = get_object_or_404(Request.objects.select_related('P_ID'), request_ID=request_id)

    data = {
        'request_id': request_instance.request_ID,
        'project_title': request_instance.Project_title,
        'request_type': request_instance.requestType,
        'driver': request_instance.Driver,
        'objective': request_instance.objective,
        'scope': request_instance.Scope,
        'requirements': request_instance.Requirments,
        'request_state': request_instance.request_state,
        'forwarded':request_instance.forwarded,
        'approved':request_instance.approved,
        'Assigned':request_instance.Assigned,
        'dep_id': request_instance.dep_ID,

        'project': {
            'P_ID': request_instance.P_ID.P_ID,
            'P_name': request_instance.P_ID.P_name,
            'P_description': request_instance.P_ID.P_description,
            'P_state': request_instance.P_ID.P_state,
            'p_budget': str(request_instance.P_ID.p_budget),  # Decimal to string
            'p_budgeted': request_instance.P_ID.p_budgeted,
            'progress': request_instance.P_ID.progress,
            'priority': request_instance.P_ID.priority,
            'requestor': request_instance.P_ID.requestor,
            'digital_starategy': request_instance.P_ID.digital_starategy,
            'digitalization': request_instance.P_ID.digitalization,
            'regulator': request_instance.P_ID.regulator,
            'p_start_date': request_instance.P_ID.p_start_date.strftime('%Y-%m-%d'),
            'p_end_date': request_instance.P_ID.p_end_date.strftime('%Y-%m-%d'),
            'Project_Manager': request_instance.P_ID.Project_Manager,
        }
    }

    return JsonResponse(data)
