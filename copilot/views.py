from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import BaseAuthentication
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from copilot.models import Users
from support.auth import Myauth
from rest_framework import serializers
# Create your views here.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class loginview(APIView):
    #authentication_classes = [Myauth,]
    def get(self, request):
        user = Users.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

        

class UserView(APIView):
    def get(self, request):
        #获取用户信息,返回用户信息
        user = Users.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
