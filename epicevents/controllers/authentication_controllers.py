from epicevents.controllers import home_controllers as home
from ..views import AuthenticationView

view = AuthenticationView()


class AuthenticationController:
    def run(self):
        while True:
            choice = view.display_menu(view.employee_menu)
            if choice == "1":
                return ...
            elif choice == "2":
                return ...
            elif choice == "3":
                return home.HomeController()
