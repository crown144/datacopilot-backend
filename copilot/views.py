from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import BaseAuthentication
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from support.auth import Myauth
# Create your views here.



class loginview(APIView):
    authentication_classes = [Myauth,]
    def get(self, request):
        #获取用户信息,返回用户信息
        user = request.user
        return Response("hello,"+user)