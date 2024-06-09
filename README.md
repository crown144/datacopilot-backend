# datacopilot-backend

## setup

1. ��װpython3.11
2. ���������� 
```
pip install -r requirements.txt
```
3. �޸�settings.py�е����ݿ�����

## run

```
python manage.py runserver --port 8080
```

## Ȩ��
��login�ӿ��⣬�����ӿ���Ҫ������ͷ�м���Authorization�ֶΣ�ֵΪ��¼�ӿڷ��ص�token

# �ӿ��ĵ�
## ��¼�ӿ�

### ����ʽ

```
POST
```

### �����ַ

```
localhost:8080/login
```
### ���ݸ�ʽ
```
{
	"username":"admin",
	"password":"admin"
}
```
### ��������
```
{
	"status": "200",
	"token": "xxx"
}
```

## ��ģ�Ͳ�ѯ�ӿ�

### �����ַ

```
localhost:8080/query/
```

### ����ʽ

```
POST
```

### ���ݸ�ʽ
```
{
	"user_input": "xxx"
}
```

### ��������
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
            "Role": "����Ա"
        },
        {
            "UserID": 3,
            "Username": "test",
            "Password": "test123",
            "Email": "test@test.com",
            "Role": "��ͨ�û�"
        }
    ]
}
```
## �û�������Ϣ��ѯ�ӿ�

### �����ַ

```
localhost:8080/UserCRUD/
```

### ����ʽ

```
GET
```

### ��������
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
### ����ʽ

```
PUT
```

### ���ݸ�ʽ
```
{
	"password": "xx"
	"email": "xx"
}
```

## ע��ӿ�

### �����ַ

```
localhost:8080/register/
```

### ����ʽ

```
POST
```

### ���ݸ�ʽ
```
{
	"username": "xx",
	"password": "xx",
	"email": "xx"
}
```

### ��������
```
{
	"status": "200",
	"message": "ע��ɹ�"
}
```

## ���ݿ��л��ӿ�
�������ȡ�������ݿ������ύ�û�ѡ��

### �����ַ

```
localhost:8080/choosesql/
```

### ����ʽ

```
GET
```

### ��������
```
{
	"status": "200",
	"databases": [
        "ai",
        "datacopilot",
    ]
}
```

### ����ʽ

```
POST
```

### ���ݸ�ʽ
```
{
	"database": "xx"
}
```

### ��������
```
{
	"status": "200",
	"message": "�л��ɹ�"
}
```

## ��ѯ��ʷ�ӿ�

### �����ַ

```
localhost:8080/history/
```

### ����ʽ

```
GET
```

### ��������
```
{
    "status": "200",
    "query_history": [
        {
            "querycontent": "��ѯ�û���Ϊuser1������",
            "formatted_querytime": "2024-06-09 21:47:04"
        }
    ]
}
```

# ״̬��

```
200: ����ɹ�
300: ���������
400: ����Ȩ�޲���
```
