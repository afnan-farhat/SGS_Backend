from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from users.views import login_view
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from users.views import login_view

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import DepartmentView, ProjectView, EmployeeLoginView, StagesViewSet, TaskViewSet
from django.urls import path
from users.views import EmployeeList, login_view
from django.http import JsonResponse
from django.urls import reverse
from users.views import EmployeeDetail
from users.views import ProjectListCreateAPIView, ProjectDetailUpdateAPIView
from users.views import extension_list

    

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the API root.",
        "available_endpoints": {
            "departments": "/departments/",
            "projects": "/projects/",
            "employee_login": "/employee-login/",
            "employees": "/employees/",
            "login": "/login/",
            "stages": "/stages/",
            "tasks": "/tasks/",
            "project-detail-update": "projects/<int:P_ID>/",
            "extension-list" : "extensions/"
            # Add any other endpoints here
        }
    })



router = DefaultRouter()
router.register(r'stages', StagesViewSet, basename='stages')
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', api_root, name='api-root'),  # API root showing available endpoints
    path('departments/', DepartmentView.as_view(), name='departments'),
    # path('projects/', ProjectView.as_view(), name='projects'),
    path('employee-login/', EmployeeLoginView.as_view(), name='employee-login'),
    path('', include(router.urls)),
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('login/', login_view, name='employee-login'),
    path('employees/<int:PRN>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('projects/<int:P_ID>/', ProjectDetailUpdateAPIView.as_view(), name='project-detail-update'),
    path('extensions/', extension_list, name='extension-list'),

]
