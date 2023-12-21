from passlib.hash import pbkdf2_sha256

from epicevents.utils.bases.controllers import BaseController
from epicevents.controllers import home_controllers as home
from ..models import EmployeeManager
from ..views import EmployeeView

view = EmployeeView()
model = EmployeeManager()


class EmployeeController(BaseController):
    def run(self):
        while True:
            choice = view.display_menu(view.employee_menu)
            if choice == "1":
                return EmployeeCreationController()
            elif choice == "2":
                return GetEmployeeByNameController()
            elif choice == "3":
                return GetEmployeeByIdController()
            elif choice == "4":
                return EmployeeModifyController()
            elif choice == "5":
                return EmployeeDeleteController()
            elif choice == "6":
                return EmployeeDisplayAll()
            elif choice == "7":
                return home.HomeController()


class EmployeeLogin(BaseController):
    def run(self):
        username = view.get_username()
        password = view.get_password()
        password_hash = ...
        return pbkdf2_sha256.verify(password, password_hash)


class EmployeeCreationController(BaseController):
    def run(self):
        employee_data = view.get_employee_data()
        model.add_employee(employee_data)
        return EmployeeController()


class GetEmployeeByNameController(BaseController):
    def run(self):
        ...
        return EmployeeController()


class GetEmployeeByIdController(BaseController):
    def run(self):
        ...
        return EmployeeController()


class EmployeeModifyController(BaseController):
    def run(self):
        ...
        return EmployeeController()


class EmployeeDeleteController(BaseController):
    def run(self):
        ...
        return EmployeeController()


class EmployeeDisplayAll(BaseController):
    def run(self):
        ...
        return EmployeeController()
