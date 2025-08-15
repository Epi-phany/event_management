from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
#from django.contrib.auth import get_user_model
from .models import User
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    # def post(self,request):
    #     data= request.data

    #     serializer = self.serializer_class(data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)