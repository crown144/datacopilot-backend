# datacopilot-backend

## setup

1. 安装python3.11
1. 命令行输入 
```
pip install -r requirements.txt
```
3. 修改settings.py中的数据库配置

## run

```
python manage.py runserver
```

## 登录接口

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
	"code": 200,
	"token": "xxx"
}
```