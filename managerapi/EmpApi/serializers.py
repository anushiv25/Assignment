from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Employee

class EmployeeSerializer(ModelSerializer):
    password = serializers.CharField(max_length = 65,min_length = 8,write_only = True) #Confidential

    class Meta:
        model = Employee

        fields = ['emp_id','firstname','lastname','password','address','dob','company','mobile','city']