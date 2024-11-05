from django.shortcuts import render
from .serializers import LoginSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import authenticate
from .tokens import  get_user_token


class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                token = get_user_token(user)
                return Response(data={'access_token': token['access_token'], 'refresh_token': token['refresh_token']}, status=200)
            else:
                return Response(data={'error': 'Invalid credentials'}, status=401)
        return Response(data={"error": "Invalid credentials"}, status=200)


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'message': 'User registered successfully'}, status=201)
        return Response(data={"error": "Invalid data"}, status=400)
    