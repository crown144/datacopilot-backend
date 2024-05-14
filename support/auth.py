from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class Myauth(BaseAuthentication):
    def authenticate(self, request):
        #从request的header中Authorization中获取token
        token = request.headers.get("Authorization")
        if token == "1":
            return ("admin", None)
        elif token == "2":
            return ("user", None)
        raise AuthenticationFailed("Failed")