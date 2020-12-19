from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import permissions

# Create your views here.
class EmployeeList(ListCreateAPIView):

    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Employee.objects.all()


class EmployeeDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "emp_id"

    def get_queryset(self):
        return Employee.objects.all()