from django.shortcuts import render
from rest_framework.fields import ReadOnlyField
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import BaseAuthentication
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from copilot.models import Users
from support.auth import Myauth
from rest_framework import serializers
import jwt
from datetime import datetime,timedelta
from backends import settings
# Create your views here.



#jwt token加密
def encode_jwt_token(username):
    payload = {
        'exp': datetime.utcnow() + timedelta(seconds=3600),  # 单位秒
        'iat': datetime.utcnow(),
        'data': {'username': username}
        }
    JWT_SECRET_KEY = settings.SECRET_KEY
    encoded_jwt = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
    return encoded_jwt

#jwt token解密
def decode_jwt_token(token):
    JWT_SECRET_KEY = settings.SECRET_KEY
    username = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
    return username


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"
        ReadOnlyField = ["userid"]

class loginview(APIView):
    #authentication_classes = [Myauth,]
    def post(self, request):
        #获取用户提交的用户名和密码
        username = request.data.get("username")
        password = request.data.get("password")
        #根据用户名和密码查询用户信息
        user = Users.objects.filter(username=username).first()
        if not user:
            return Response({"message": "用户名不存在"})
        #返回用户信息
        else:
            serializer = UserSerializer(user)
            #检查密码是否正确
            if password != user.password:
                return Response({"message": "密码错误"})
            else:
                token = ""
        #返回status code 200和token
        msg={"status": "200", "token": token}
        return Response(msg)


        

class UserView(APIView):
    authentication_classes = [Myauth,]
    def get(self, request):
        #获取用户信息,返回用户信息
        user = Users.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
