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
from support.LLM import SQLQueryGenerator
from django.db import connection
from support.jwt_token import JWTToken
# Create your views here.



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
                #用户名加密成token
                jwt = JWTToken()
                token = jwt.encode(username)
                #返回status code 200和token
                msg={"status": "200", "token": token}
                return Response(msg)


        

class QueryView(APIView):
    authentication_classes = [Myauth,]
    def post(self, request):
        #获取用户输入的自然语言
        user_input = request.data.get("user_input")
        # print(user_input)
        # #实例化类
        # sql_generater = SQLQueryGenerator()
        # #调用函数生成SQL查询语句
        # sql_queries = sql_generater.generate_sql_query(user_input)
        # #用SQL语句查询数据库
        # sql_query = sql_queries[0].strip()
        # with connection.cursor() as cursor:
        #     # 执行SQL查询
        #     cursor.execute(sql_query)
    
        #     # 获取所有查询结果
        #     results = cursor.fetchall()
    
        #返回status code 200和查询结果
        msg = {"status": "200", "sql_queries": request.user}
        return Response(msg)
