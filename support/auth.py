from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class Myauth(BaseAuthentication):
    def authenticate(self, request):
        #��request��header��Authorization�л�ȡtoken
        token = request.headers.get("Authorization")
        if token == "1":
            return ("admin", None)
        elif token == "2":
            return ("user", None)
        raise AuthenticationFailed("Failed")