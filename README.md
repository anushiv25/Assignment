# Assignment
SwaggerAPI implemented for Manager and Employee management system.

# Installation:
1) Install python 3 and add it to the path
2) Install Django version 2.2.16 => pip install Django==2.2.16
3) Install Django Rest Framework using => pip install djangorestframework
4) Install Swagger API for Django => pip install drf-yasg

# Running:
=>In settings.py remove the current JWT Secret Key and add it manually when deploying it globally. For testing purpose let it be as it is.
=>Go to the manage.py location and open terminal then run command - python manage.py runserver
=>Open the address given in terminal after running the server in browser

# Testing on Browser:
=>Using '/auth/register' register a new User(Manager).
=>Using '/auth/login' login the user previously created and copy the token when successfully logged in.
=>Click on Authorize Button then type in the box 'Bearer' space 'the token that you have just copied'.
For example - Bearer adbcaicbkiUQISUWH.UCBUKJADVJCHSj
=>Now click on authorize button
=>Now you are successfully logged in and can test adding employee and other functionalities.