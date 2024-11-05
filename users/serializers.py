from rest_framework import serializers
from django.contrib.auth.models import User
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
import re


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

# class RegisterSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=255, required=True)
#     password = serializers.CharField(max_length=128, required=True)
#     first_name = serializers.CharField(max_length=30, required=False)
#     last_name = serializers.CharField(max_length=30, required=False)
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email', 'password', 'first_name', 'last_name')





    def validate_email(self,email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        return email
    
    
    def validate_password(self,value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")
        if not re.search(r'[!@#$%^\*(),.?":{}|<>_]', value):
            raise serializers.ValidationError("Parolda kamida bitta maxsus belgi bo‘lishi kerak.")
        return value
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
