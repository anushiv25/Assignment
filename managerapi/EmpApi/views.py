from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import permissions

#Listing and Creating all the employees
class EmployeeList(ListCreateAPIView):

    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Employee.objects.all()


#Retrieving, Updating, Deleting the employee
class EmployeeDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "emp_id"

    def get_queryset(self):
        return Employee.objects.all()