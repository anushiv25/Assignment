#Implementing Custom User Model as email is used in place of Username.
from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager, PermissionsMixin)

from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, username, email, firstname, lastname, address, dob, company, password=None):

        if username is None:
            raise TypeError('Users should have a Username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            firstname = firstname,
            lastname = lastname,
            address = address,
            dob = dob,
            company = company
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):

        if password is None:
            raise TypeError('Password should not be None')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


#Manager data is stored in this table
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    company = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email' #To use email and password for authentication
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return email