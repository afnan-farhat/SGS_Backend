from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Department, Project, Employee, Stages, Task
from .serializers import DepartmentSerializer, ProjectSerializer, EmployeeSerializer, StagesSerializer, TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from .models import Employee
from .serializers import EmployeeSerializer
from .serializers import ProjectSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from .models import Project
from rest_framework.generics import ListCreateAPIView

from rest_framework import generics
# 1. Department: Only GET (read-only)
class DepartmentView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)


# 2. Project: GET and POST (for JSON file)
class ProjectView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProjectDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'P_ID'  

from .serializers import ProjectSerializer

class ProjectListCreateAPIView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# 3. Employee: GET (as login, based on PRN or email)


# List all employees (GET)
class EmployeeList(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


# Login view (POST using email only)
@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')

    try:
        employee = Employee.objects.get(Email=email)  # Use 'Email' with exact field name
        return Response({
            "success": True,
            "PRN": employee.PRN,
            "Emp_name": employee.Emp_name,
            "Emp_role": employee.Emp_role,
            "Job_title": employee.Job_title,
            "Email": employee.Email,
            "Chat": employee.Chat,
            "Work_phone": employee.Work_phone,
            "Buisness_address": employee.Buisness_address,
        })
    except Employee.DoesNotExist:
        return Response({"success": False, "error": "Invalid email"}, status=status.HTTP_400_BAD_REQUEST)

class EmployeeLoginView(APIView):
    def get(self, request):
        prn = request.query_params.get('PRN', None)
        email = request.query_params.get('Email', None)

        if prn:
            try:
                employee = Employee.objects.get(PRN=prn)
            except Employee.DoesNotExist:
                return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        elif email:
            try:
                employee = Employee.objects.get(Email=email)
            except Employee.DoesNotExist:
                return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "PRN or Email required"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)




class EmployeeDetail(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'PRN'

# 4. (Optional) Stages: Full CRUD
class StagesViewSet(viewsets.ModelViewSet):
    queryset = Stages.objects.all()
    serializer_class = StagesSerializer


# 5. (Optional) Task: Full CRUD
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
