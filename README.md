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
python manage.py runserver
```

## Ȩ��
��login�ӿ��⣬�����ӿ���Ҫ������ͷ�м���token�ֶΣ�ֵΪ��¼�ӿڷ��ص�token

# �ӿ��ĵ�
## ��¼�ӿ�

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
	"code": 200,
	"token": "xxx"
}
```

## ��ģ�Ͳ�ѯ�ӿ�

### �����ַ

```
localhost:8080/query/
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
    "sql_queries": {
        "UserID": 3,
        "Username": "test",
        "Password": "test123",
        "Email": "test@test.com",
        "Role": "��ͨ�û�"
    }
}
```