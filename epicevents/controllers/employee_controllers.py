import time
import logging

from sqlalchemy.exc import IntegrityError

from ..utils.bases.controllers import BaseController
from ..utils.contants import SHORT_SLEEP
from ..models import EmployeeManager, RoleManager
from ..views import employee_views, role_views
from ..controllers import home_controllers

view = employee_views.EmployeeView()
manager = EmployeeManager()
role_manager = RoleManager()
role_view = role_views.RoleView()


class EmployeeController(BaseController):
    def run(self):
        while True:
            choice = view.menu_choice()
            if choice == "1":
                return EmployeeCreationController()
            elif choice == "2":
                return EmployeeUpdateController()
            elif choice == "3":
                return EmployeeDeleteController()
            elif choice == "4":
                return EmployeeDisplayAllController()
            elif choice == "5":
                return home_controllers.HomeController()


class EmployeeCreationController(BaseController):
    def run(self):
        roles = role_manager.get_all_roles()
        role_view.display_roles_table(roles)

        view.display_create_employee()
        employee_data = view.get_employee_data()
        try:
            manager.create_employee(**employee_data)
            view.success_creating()
            return EmployeeController()
        except IntegrityError as e:
            logging.error(f"IntegrityError: {e}")
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


class EmployeeUpdateController(BaseController):
    def run(self):
        employees = manager.get_all_employee()
        view.display_employee_table(employees=employees)

        employee_id = view.get_employee_id()
        try:
            employee = manager.get_employee_by_id(employee_id=employee_id)
            if employee:
                roles = role_manager.get_all_roles()
                role_view.display_roles_table(roles)

                employee_data = view.get_employee_data()
                manager.update_employee(
                    employee_id=employee_id, **employee_data
                )
                view.success_update()
            else:
                view.not_found()
        except Exception as e:
            logging.exception(f"Unexpected error during employee update: {e}")
        finally:
            return EmployeeController()


class EmployeeDeleteController(BaseController):
    def run(self):
        employees = manager.get_all_employee()
        view.display_employee_table(employees=employees)

        employee_id = view.get_employee_id()
        deleted = manager.delete_employee(employee_id=employee_id)
        if deleted:
            view.success_delete()
        else:
            view.not_found()
        return EmployeeController()


class EmployeeDisplayAllController(BaseController):
    def run(self):
        employees = manager.get_all_employee()
        view.display_employee_table(employees=employees)
        return EmployeeController()


class EmployeeLoginController(BaseController):
    def run(self):
        max_attempts = 3
        for _ in range(max_attempts):
            view.display_login()
            username = view.get_username()
            get_username = manager.get_employee_by_username(username=username)
            if get_username:
                password_hash = manager.get_employee_password_by_username(
                    username=username
                )
                decode = view.test_decode_password(password_hash=password_hash)
                if decode:
                    return home_controllers.HomeController()
                else:
                    view.not_found()
            else:
                view.not_found()
        return None
