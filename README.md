# datacopilot-backend

## setup

1. 安装python3.11
2. 命令行输入 
```
pip install -r requirements.txt
```
3. 修改settings.py中的数据库配置

## run

```
python manage.py runserver --port 8080
```

## 权限
除login接口外，其他接口需要在请求头中加入Authorization字段，值为登录接口返回的token

# 接口文档
## 登录接口

### 请求方式

```
POST
```

### 请求地址

```
localhost:8080/login
```
### 数据格式
```
{
	"username":"admin",
	"password":"admin"
}
```
### 返回数据
```
{
	"status": "200",
	"token": "xxx"
}
```

## 大模型查询接口

### 请求地址

```
localhost:8080/query/
```

### 请求方式

```
POST
```

### 数据格式
```
{
	"user_input": "xxx"
}
```

### 返回数据
```
{
    "status": "200",
    "sql_queries": [
        {
            "UserID": 1,
            "Username": "root",
            "Password": "root123",
            "Email": "root@example.com",
            "Role": ""
        },
        {
            "UserID": 2,
            "Username": "root",
            "Password": "root123",
            "Email": "root@example.com",
            "Role": "管理员"
        },
        {
            "UserID": 3,
            "Username": "test",
            "Password": "test123",
            "Email": "test@test.com",
            "Role": "普通用户"
        }
    ]
}
```
## 用户基本信息查询接口

### 请求地址

```
localhost:8080/UserCRUD/
```

### 请求方式

```
GET
```

### 返回数据
```
{
	"status": "200",
	"users": [
		{
			"username": "xx",
			"password": "xx",
			"email": "xx"
		}
	]
}
```
### 请求方式

```
PUT
```

### 数据格式
```
{
	"password": "xx"
	"email": "xx"
}
```

## 注册接口

### 请求地址

```
localhost:8080/register/
```

### 请求方式

```
POST
```

### 数据格式
```
{
	"username": "xx",
	"password": "xx",
	"email": "xx"
}
```

### 返回数据
```
{
	"status": "200",
	"message": "注册成功"
}
```


# 状态码

```
200: 请求成功
300: 无相关数据
400: 请求权限不足
```
