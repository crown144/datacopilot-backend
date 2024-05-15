from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from support.jwt_token import JWTToken

class Myauth(BaseAuthentication):
    def authenticate(self, request):
        #��request��header��Authorization�л�ȡtoken
        token = request.headers.get("Authorization")
        #ʵ����JWTToken��
        jwt = JWTToken()
        #����token
        payload = jwt.decode(token)
        username = payload.get("data").get("username")
        if username:
            return (username, token)
        else:
            raise AuthenticationFailed("Failed")