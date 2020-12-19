from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 65,min_length = 8,write_only = True)
    email = serializers.EmailField(max_length = 255)

    class Meta:
        model = User
        fields = ['username','email','firstname','lastname',
        'address','dob','company','password']

    
    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(
                {'email':('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=5)

    class Meta:
        model = User
        fields = ['email', 'password']