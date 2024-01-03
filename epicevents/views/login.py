from passlib.hash import pbkdf2_sha256
from epicevents.utils.bases.views import BaseView


class Login(BaseView):
    def get_login(self):
        username = self._get_username()
        password = self._get_password()
        return username, password

    def code_login(self, password):
        return pbkdf2_sha256.using(salt_size=64).hash(password)

    def decode_login(self, password_hash):
        return  # decode password_hash

    def verify_login(self, password, password_hash):
        return pbkdf2_sha256.verify(password, password_hash)


login = Login()

# Exemple d'utilisation
username, password = login.get_login()
password_hash = login.decode_login(password)
print(password_hash)

entered_password = "motdepasse123"
if login.verify_login(entered_password, password_hash):
    print("Connexion réussie")
else:
    print("Échec de la connexion")
