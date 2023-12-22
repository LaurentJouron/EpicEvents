from passlib.hash import pbkdf2_sha256
from epicevents.utils.bases.views import BaseView


class Login(BaseView):
    def get_login(self):
        username = self._get_username()
        lastname = self._get_lastname()
        password = self.code_login()
        return username, lastname, password

    def code_login(self):
        password = self._get_password()
        password_hash = pbkdf2_sha256.using(salt_size=64).hash(password)
        return password_hash

    def decode_login(self, password_hash):
        password = self._get_password()
        hash = password_hash
        return pbkdf2_sha256.verify(password, hash)


login = Login()
print(login.get_login())
password_hash = login.code_login()
print(password_hash)
password_decode = login.decode_login(password_hash)
print(password_decode)
