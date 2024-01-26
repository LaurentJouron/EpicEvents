from ..utils.bases.controllers import BaseController
from ..utils.contants import FILEPATH, GESTION
from ..models import EmployeeManager, DepartmentManager
from ..views.employee_views import EmployeeView
from ..views.department_views import DepartmentView
from ..controllers import home_controllers
import logging
import json
import os

from sqlalchemy.exc import IntegrityError
from passlib.hash import pbkdf2_sha256


view = EmployeeView()
manager = EmployeeManager()


class EmployeeController(BaseController):
    def run(self):
        employee_login = EmployeeLoginController()
        employee = employee_login.read_login_file()
        while True:
            choice = view.menu_choice()
            if choice == "1":
                # Création uniquement si departement == Gestion
                if employee["department_id"] == GESTION:
                    return EmployeeCreateController()
                else:
                    view.error_not_have_right()
                    return EmployeeController()

            elif choice == "2":
                return EmployeeReadController()

            elif choice == "3":
                # Modification uniquement si departement == Gestion
                if employee["department_id"] == GESTION:
                    return EmployeeUpdateController()
                else:
                    view.error_not_have_right()
                    return EmployeeController()

            elif choice == "4":
                # Suppression uniquement si departement == Gestion
                if employee["department_id"] == GESTION:
                    return EmployeeDeleteController()
                else:
                    view.error_not_have_right()
                    return EmployeeController()

            elif choice == "5":
                return home_controllers.HomeController()

    def get_data(self):
        username = view.get_username()
        last_name = view.get_lastname()
        email = view.get_email()
        phone = view.get_phone()
        password = view.encoded_password()
        department_id = self.get_department_id()
        return {
            "username": username,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "password": password,
            "department_id": department_id,
        }

    def get_department_id(self):
        department_manager = DepartmentManager()
        department_view = DepartmentView()
        departments = department_manager.read()
        department_view.display_table(departments)
        return view.select_id()


class EmployeeCreateController(EmployeeController):
    def run(self):
        view.display_title("Create employee")
        data = self.get_data()
        try:
            manager.create(**data)
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


class EmployeeReadController(EmployeeController):
    def run(self):
        employees = manager.read()
        view.display_table(employees=employees)
        return EmployeeController()


class EmployeeUpdateController(EmployeeController):
    def run(self):
        employees = manager.read()
        view.display_table(employees=employees)
        employee_id = view.select_id()

        try:
            employee = manager.get_by_id(employee_id=employee_id)

            if employee:
                employee_data = self.get_data()
                manager.update(employee_id=employee_id, **employee_data)
                view.success_update()
            else:
                view.error_not_found()

        except Exception as e:
            logging.exception(f"Unexpected error during employee update: {e}")
        finally:
            return EmployeeController()


class EmployeeDeleteController(EmployeeController):
    def run(self):
        employees = manager.read()
        view.display_table(employees=employees)
        employee_id = view.select_id()
        deleted = manager.delete(employee_id=employee_id)

        if deleted:
            view.success_delete()
        else:
            view.not_found()
        return EmployeeController()


class EmployeeLoginController(EmployeeController):
    def run(self):
        token = self.search_token()

        if token != "":
            return home_controllers.HomeController()
        else:
            max_attempts = 3

            for _ in range(max_attempts):
                view.display_title("Login")
                username = view.get_username()
                employee = manager.get_by_username(username=username)

                if employee:
                    password_hash = manager.get_password(username=username)

                    if view.test_decode_password(password_hash=password_hash):
                        data = self.get_data_log(username=username)

                        for key, value in data.items():
                            self.write_login_file(key, value)
                        return home_controllers.HomeController()
                view.error_not_found()
            return None

    def write_login_file(self, key, value):
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

    def read_login_file(self):
        if not os.path.exists(FILEPATH):
            return {}

        try:
            with open(FILEPATH, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            return {}
        return data

    def login_file(self):
        with open(FILEPATH) as f:
            return json.load(f)["employee_id"]

    def create_token(self, username):
        return pbkdf2_sha256.using(salt_size=64).hash(username)

    def search_token(self):
        with open(FILEPATH) as f:
            return json.load(f)["token"]

    def get_data_log(self, username):
        department_id = manager.get_department_id_by_username(
            username=username
        )
        employee_id = manager.get_id_by_username(username=username)
        token = self.create_token(username=username)
        return {
            "employee_id": employee_id,
            "department_id": department_id,
            "token": token,
        }


class EmployeeLogoutController(EmployeeController):
    def run(self):
        with open(FILEPATH, "w") as f:
            return json.dump(
                {
                    "employee_id": 0,
                    "department_id": 0,
                    "token": "",
                },
                f,
                indent=4,
            )
