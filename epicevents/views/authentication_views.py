from epicevents.utils.bases.menus import BaseMenu


class AuthenticationView(BaseMenu):
    authentication_menu: dict = {
        "1": "First connexion",
        "2": "Login",
        "3": "Return",
    }
