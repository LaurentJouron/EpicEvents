import logging
import json
import os
from ..utils.bases.controllers import BaseController
from ..utils.contants import FILEPATH
from ..models import EmployeeManager, RoleManager
from ..views import employee_views, role_views
from ..controllers import home_controllers

from sqlalchemy.exc import IntegrityError
from passlib.hash import pbkdf2_sha256


view = employee_views.EmployeeView()
manager = EmployeeManager()


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
        view.display_create_employee()
        employee_data = self.get_employee_data()
        try:
            manager.create_employee(**employee_data)
            view.success_creating()
            return EmployeeController()
        except IntegrityError as e:
            logging.error(f"IntegrityError: {e}")

            return EmployeeController()
        except Exception as e:
            logging.exception(f"Unexpected error: {e}")

            raise
        finally:
            EmployeeController()

    def get_employee_data(self):
        username = view.get_username()
        last_name = view.get_lastname()
        email = view.get_email()
        phone = view.get_phone_number()
        password = view.encoded_password()
        role_id = self.get_role_id()
        return {
            "username": username,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "password": password,
            "role_id": role_id,
        }

    def get_role_id(self):
        role_manager = RoleManager()
        role_view = role_views.RoleView()
        roles = role_manager.get_all_roles()
        role_view.display_roles_table(roles)
        return view.select_id()


class EmployeeUpdateController(EmployeeCreationController):
    def run(self):
        employees = manager.get_all_employee()
        view.display_employee_table(employees=employees)

        employee_id = view.get_employee_id()
        try:
            employee = manager.get_employee_by_id(employee_id=employee_id)
            if employee:
                employee_data = self.get_employee_data()
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


class EmployeeCommercialController(EmployeeController):
    def run(self):
        ...


class EmployeeGestionController(EmployeeController):
    def run(self):
        ...


class EmployeeSupportController(EmployeeController):
    def run(self):
        ...


class EmployeeLoginController(BaseController):
    def run(self):
        token = self.search_token()
        if token != 0:
            return home_controllers.HomeController()
        else:
            max_attempts = 3
            for _ in range(max_attempts):
                view.display_login()
                username = view.get_username()
                employee = manager.get_by_username(username=username)

                if employee:
                    password_hash = manager.get_password(username=username)
                    if view.test_decode_password(password_hash=password_hash):
                        data = self.get_data_log(username=username)
                        for key, value in data.items():
                            self.write_on_json_file(key, value)
                        return home_controllers.HomeController()
                view.not_found()
            return None

    def write_on_json_file(self, key, value):
        if not os.path.exists(FILEPATH):
            with open(FILEPATH, "w") as f:
                json.dump({}, f)
        try:
            with open(FILEPATH, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {}
        data[key] = value
        with open(FILEPATH, "w") as f:
            json.dump(data, f, indent=4)

    def create_token(self, username):
        return pbkdf2_sha256.using(salt_size=64).hash(username)

    def search_token(self):
        with open(FILEPATH) as f:
            return json.load(f)["token"]

    def login_file_employee_id(self):
        with open(FILEPATH) as f:
            return json.load(f)["employee_id"]

    def get_data_log(self, username):
        role_id = manager.role_id_by_username(username=username)
        employee_id = manager.get_id_by_username(username=username)
        token = self.create_token(username=username)
        return {
            "employee_id": employee_id,
            "role_id": role_id,
            "token": token,
        }

    def redirect_employee(self):
        with open(FILEPATH) as f:
            role = json.load(f)["role_id"]
            role = str(role)
            if role == "1":
                # Commercial
                return home_controllers.HomeCommercialController()
            elif role == "2":
                # Gestion
                return home_controllers.HomeGestionController()
            elif role == "3":
                # Support
                return home_controllers.HomeSupportController()
            else:
                view.not_found()
                return


class EmployeeLogoutController(BaseController):
    def run(self):
        with open(FILEPATH, "w") as f:
            return json.dump(
                {
                    "employee_id": 0,
                    "role_id": 0,
                    "token": 0,
                },
                f,
                indent=4,
            )
