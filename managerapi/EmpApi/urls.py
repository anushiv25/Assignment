from django.urls import path
from .views import EmployeeList, EmployeeDetailView


urlpatterns = [
    path('', EmployeeList.as_view()),
    path('<slug:emp_id>', EmployeeDetailView.as_view()),
]