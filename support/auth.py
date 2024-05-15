from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from support.jwt_token import JWTToken

class Myauth(BaseAuthentication):
    def authenticate(self, request):
        #从request的header中Authorization中获取token
        token = request.headers.get("Authorization")
        #实例化JWTToken类
        jwt = JWTToken()
        #解密token
        payload = jwt.decode(token)
        username = payload.get("data").get("username")
        if username:
            return (username, token)
        else:
            raise AuthenticationFailed("Failed")