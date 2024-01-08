import time
import logging

from sqlalchemy.exc import IntegrityError

from ..utils.bases.controllers import BaseController
from ..utils.contants import LONG_SLEEP, SHORT_SLEEP
from ..models import EmployeeManager
from ..views import employee_views
from ..controllers import home_controllers

view = employee_views.EmployeeView()
manager = EmployeeManager()


class EmployeeController(BaseController):
    def run(self):
        while True:
            choice = view.menu_choice()
            if choice == "1":
                return EmployeeCreationController()
            elif choice == "2":
                return UpdateEmployeeController()
            elif choice == "3":
                return GetEmployeeUsernameByIdController()
            elif choice == "4":
                return GetEmployeeIdByUsernameController()
            elif choice == "5":
                return EmployeeDeleteController()
            elif choice == "6":
                return EmployeeDisplayAll()
            elif choice == "7":
                return home_controllers.HomeController()


class EmployeeCreationController(BaseController):
    def run(self):
        employee_data = view.get_employee_data()
        try:
            manager.create_employee(**employee_data)
            view.success_creating()
            time.sleep(SHORT_SLEEP)
            view.clean_console()
            return EmployeeController()
        except IntegrityError as e:
            logging.error(f"IntegrityError: {e}")
            view.exist_error(employee_data)
            time.sleep(SHORT_SLEEP)
            view.clean_console()
            return EmployeeController()
        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            time.sleep(SHORT_SLEEP)
            view.clean_console()
            raise
        finally:
            EmployeeController()


class UpdateEmployeeController(BaseController):
    def run(self):
        print("UpdateEmployeeController")
        view._success_updated()
        time.sleep(LONG_SLEEP)
        view.clean_console()
        return EmployeeController()


class GetEmployeeUsernameByIdController(BaseController):
    def run(self):
        print("GetEmployeeUsernameByIdController")
        time.sleep(LONG_SLEEP)
        view.clean_console()
        return EmployeeController()


class GetEmployeeIdByUsernameController(BaseController):
    def run(self):
        print("GetEmployeeIdByUsernameController")
        time.sleep(LONG_SLEEP)
        view.clean_console()
        return EmployeeController()


class EmployeeDeleteController(BaseController):
    def run(self):
        print("EmployeeDeleteController")
        view._success_delete()
        time.sleep(LONG_SLEEP)
        view.clean_console()
        return EmployeeController()


class EmployeeDisplayAll(BaseController):
    def run(self):
        employees = manager.get_all_employee()
        view.display_employee_table(employees=employees)
        return EmployeeController()
