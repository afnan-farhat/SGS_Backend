# users/serializers.py
from rest_framework import serializers
from .models import Department, Project, Employee, Stages, Task, Manages

# 1. Department Serializer


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

# 3. Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


# 4. Manages Serializer
class ManagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manages
        fields = '__all__'


# 4. Stages Serializer
class StagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stages
        fields = '__all__'


# 5. Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

