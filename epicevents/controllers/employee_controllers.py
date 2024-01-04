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
                return home_controllers.HomeController()


class EmployeeCreationController(BaseController):
    def run(self):
        employee = view.get_employee_data()
        try:
            manager.add_employee(employee)
            view.success_creating()
            time.sleep(SHORT_SLEEP)
            view.clean_console()
            return EmployeeController()
        except IntegrityError as e:
            logging.error(f"IntegrityError: {e}")
            view.exist_error(employee)
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
        view._success_updated()
        time.sleep(LONG_SLEEP)
        view.clean_console()
        return EmployeeController()


class EmployeeDeleteController(BaseController):
    def run(self):
        ...
        view._success_delete()
        time.sleep(LONG_SLEEP)
        view.clean_console()
        return EmployeeController()


class EmployeeDisplayAll(BaseController):
    def run(self):
        ...
        return EmployeeController()
