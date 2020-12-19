from django.db import models
from django.conf import settings
from authentication.models import User
from django.core.validators import RegexValidator

#Employee Table
class Employee(models.Model):
    emp_id = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    company = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15, validators=[RegexValidator(r'^\d{1,10}$')])
    city = models.CharField(max_length=100)

    class Meta:
        ordering = ['firstname', 'lastname'] #To retreive data first by firstname then by lastname

    def __str__(self):
        return emp_id