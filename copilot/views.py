from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import BaseAuthentication
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from support.auth import Myauth
from rest_framework import serializers
from copilot.models import Users
# Create your views here.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class loginview(APIView):
    # authentication_classes = [Myauth,]
    def get(self, request):
        # 创建一个新的Users实例
        new_user = Users(username='root', password='root123', email='root@example.com', role='管理员')
        # 保存到数据库
        new_user.save()
        user = Users.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

class UserView(APIView):
    def get(self, request):
        # 获取用户信息,返回用户信息
        user = Users.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)