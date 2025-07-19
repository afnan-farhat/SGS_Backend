# users/serializers.py
from rest_framework import serializers
from .models import UserProject  

from .models import Request

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProject
        fields = '__all__'



class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
            'request_ID',
            'Project_title',
            'requestType',   # لاحظ نفس اسم الحقل في الموديل
            'Driver',
            'objective',
            'Scope',
            'Requirments',
            'request_state',
            'dep_ID',
        ]



