from datetime import datetime, timedelta
import jwt
from backends import settings

#讲下面两个函数封装到一个类中


class JWTToken():
    def __init__(self):
        pass

    def encode(self, username):
        payload = {
            'exp': datetime.utcnow() + timedelta(seconds=3600),  # 单位秒
            'iat': datetime.utcnow(),
            'data': {'username': username}
            }
        encoded_jwt = jwt.encode(payload,settings.SECRET_KEY , algorithm='HS256')
        return encoded_jwt

    def decode(self, token):
        username = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return username