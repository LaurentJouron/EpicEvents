from epicevents.controllers import home_controllers as home
from views import EmployeeView

view = EmployeeView()


class EmployeeController:
    def run(self):
        while True:
            choice = view.display_menu(view.employee_menu)
            if choice == "1":
                return EmployeeCreationController()
            elif choice == "2":
                return EmployeeModifyController()
            elif choice == "3":
                return EmployeeDeleteController()
            elif choice == "4":
                return EmployeeDisplayAll()
            elif choice == "5":
                return home.HomeController()


class EmployeeCreationController:
    def run(self):
        ...
        return EmployeeController()


class EmployeeModifyController:
    def run(self):
        ...
        return EmployeeController()


class EmployeeDeleteController:
    def run(self):
        ...
        return EmployeeController()


class EmployeeDisplayAll:
    def run(self):
        ...
        return EmployeeController()
