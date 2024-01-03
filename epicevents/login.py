import jwt
from utils.bases.views import BaseView


class Login(BaseView):
    def encode(self):
        key = "secret"
        username = self._get_username()
        # password = self._get_password()
        encoded = jwt.encode({"username": username}, key, algorithm="HS256")
        print(encoded)

    def decode(self):
        ...

    def signup(self):
        ...


login = Login()
login.encode()
