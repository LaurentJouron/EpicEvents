from epicevents.views.utils.bases.controllers import BaseController

from ..models import EmployeeManager
from ..views import EmployeeView
from ..controllers import home_controllers

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
                return home_controllers()


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
