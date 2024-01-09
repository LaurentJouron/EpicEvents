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
                view.clean_console()
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
                return EmployeeDisplayAllController()
            elif choice == "7":
                return home_controllers.HomeController()


class EmployeeCreationController(BaseController):
    def run(self):
        view.display_create_employee()
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


class EmployeeDisplayAllController(BaseController):
    def run(self):
        employees = manager.get_all_employee()
        view.display_employee_table(employees=employees)
        return EmployeeController()


class EmployeeLoginController(BaseController):
    def run(self):
        # Limit the number of tests to avoid an infinite loop
        max_attempts = 3

        for _ in range(max_attempts):
            view.display_login()
            username = view.get_username()
            confirm_username = manager.get_employee_by_username(
                username=username
            )

            if confirm_username:
                password_hash = manager.get_employee_password_by_username(
                    username=username
                )
                test_decode = view.test_decode_password(
                    password_hash=password_hash
                )

                if test_decode:
                    view.clean_console()
                    return home_controllers.HomeController()
                else:
                    view.not_found(confirm_username)
                    time.sleep(LONG_SLEEP)
                    view.clean_console()
            else:
                view.not_found(username)

        # If the user reaches the maximum number of unsuccessful attempts
        view.clean_console()
        return None
