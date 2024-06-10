from glob import iglob
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
from support.sqldata import DatabaseMetadata
from support.sqlquery import DatabaseConnection
from datetime import datetime
from copilot.models import Queries
from django.utils import timezone
# Create your views here.



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'password', 'email')
        

class queryhistorySerializer(serializers.ModelSerializer):
    formatted_querytime = serializers.SerializerMethodField()

    class Meta:
        model = Queries
        fields = ('querycontent', 'formatted_querytime','queryid','userid')

    def get_formatted_querytime(self, obj):
        return obj.querytime.strftime('%Y-%m-%d %H:%M:%S')


class loginView(APIView):
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


class registerView(APIView):
    def post(self, request):
        #获取用户提交的用户名、密码和邮箱
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        #检查用户是否已经存在
        user = Users.objects.filter(username=username).first()
        if user:
            return Response({"message": "用户名已存在"})
        #创建用户
        user = Users.objects.create(username=username, password=password, email=email,role='普通用户')
        #保存用户信息
        user.save()
        msg = {"status": "200", "message": "注册成功"}
        return Response(msg)

class QueryView(APIView):
    authentication_classes = [Myauth,]
    def post(self, request):
        #获取用户输入的自然语言
        user_input = request.data.get("user_input")
        # print(user_input)
        #实例化类
        sql_generater = SQLQueryGenerator()
        #调用函数生成SQL查询语句
        sql_query = sql_generater.generate_sql_query(user_input)
        print(sql_query)
        if("DROP" in sql_query or "DELETE" in sql_query or "UPDATE" in sql_query or "INSERT" in sql_query):
            if(request.user != "admin"):
                return Response({"status": "400","content":"不允许进行该操作"})
        try:
           db_connection = DatabaseConnection()
           db_connection.connect()
           database = request.data.get('database')
           print(database)
           results = db_connection.execute_query(sql_query, database_name=database)

        except:
            return Response({"status": "300","content":"查询错误"})
        finally:
            db_connection.close()
        #返回status code 200和查询结果
        msg = {"status": "200", "sql_queries": results}
        #将用户查询信息保存到数据库
        username = request.user
        #通过用户名查询用户ID
        user = Users.objects.filter(username=username).first()
        query = Queries.objects.create(userid=user, querycontent=user_input, querytime=datetime.now())
        query.save()
        return Response(msg)

class UserCRUDView(APIView):
    authentication_classes = [Myauth,]
    def get(self, request):
        #获取当前用户信息
        now_user = request.user
        #print(now_user)
        user = Users.objects.filter(username=now_user)
        #序列化用户信息
        serializer = UserSerializer(user, many=True)
        #返回status code 200和用户信息
        msg = {"status": "200", "users": serializer.data}
        return Response(msg)

    def put(self, request):
        #获取当前用户信息
        now_user = request.user
        #print(now_user)
        user = Users.objects.filter(username=now_user).first()
        #获取用户提交的用户名、密码和邮箱
        password = request.data.get("password")
        email = request.data.get("email")
        #更新用户信息
        if password:
            user.password = password
        if email:
            user.email = email

        #保存用户信息
        user.save()
        msg = {"status": "200", "message": "更新成功"}
        return Response(msg)

class choosesqlView(APIView):
    authentication_classes = [Myauth,]
    def get(self, request):
        #获取所有数据库名
        with connection.cursor() as cursor:
            cursor.execute("show databases")
            results = cursor.fetchall()
            #将数据库名转换成列表
            db_list = [result[0] for result in results]
            #返回status code 200和数据库名
            msg = {"status": "200", "databases": db_list}
            return Response(msg)
    def post(self,request):
        #获取用户提交的数据库名
        database = request.data.get("database")
        #保存数据库名到session
        request.session['selected_database'] = database
        request.session.set_expiry(0)
        request.session.save()
        #获取数据库中所有表名
        db_metadata = DatabaseMetadata(database)
        metadata = db_metadata.get_metadata()
        #保存元数据到 JSON 文件
        db_metadata.save_metadata_to_json('support/metadata_layer.json')
        return Response({"status": "200", "message": "切换成功"})
    
class queryhistoryView(APIView):
    authentication_classes = [Myauth,]
    def get(self, request):
        #获取当前用户信息
        now_user = request.user
        #通过用户名查询用户ID
        user = Users.objects.filter(username=now_user).first()
        #通过用户ID查询用户查询历史
        query = Queries.objects.filter(userid=user)
        #序列化用户查询历史
        serializer = queryhistorySerializer(query, many=True)
        
        #返回status code 200和用户查询历史
        msg = {"status": "200", "query_history": serializer.data}
        return Response(msg)

class testView(APIView):
    def get(self, request):
        database = request.session.get('selected_database')
        return Response({"status": "200", "message": database})