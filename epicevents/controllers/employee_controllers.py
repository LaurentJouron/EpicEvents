from ..utils.bases.controllers import BaseController
from ..utils.contants import FILEPATH, GESTION
from ..models.employee import Employee
from ..models import EmployeeManager, DepartmentManager
from ..views.employee_views import EmployeeView
from ..controllers import home_controllers
from ..controllers.department_controllers import DepartmentController
import logging
import json
import os

from sqlalchemy.exc import IntegrityError
from passlib.hash import pbkdf2_sha256
from rich.table import Table
from rich.console import Console

console = Console()
view = EmployeeView()
manager = EmployeeManager()


class EmployeeController(BaseController):
    """Controller for managing employees."""

    def run(self):
        """Run the employee controller.

        Returns:
            EmployeeCreateController or EmployeeReadController or
            EmployeeUpdateController or EmployeeDeleteController or
            home_controllers.HomeController: The next controller to run
            based on user choice.
        """
        department = self.get_user_login_department()
        while True:
            choice = view.menu_choice()
            if choice == "1":
                if department == GESTION:
                    return EmployeeCreateController()
                view.error_not_have_right()
                return EmployeeController()

            elif choice == "2":
                return EmployeeReadController()

            elif choice == "3":
                if department == GESTION:
                    return EmployeeUpdateController()
                view.error_not_have_right()
                return EmployeeController()

            elif choice == "4":
                if department == GESTION:
                    return EmployeeDeleteController()
                view.error_not_have_right()
                return EmployeeController()

            elif choice == "5":
                return home_controllers.HomeController()

    def get_data(self):
        """Get employee data from user input.

        Returns:
            dict: The employee data.
        """
        username = view.get_username()
        last_name = view.get_lastname()
        email = view.get_email()
        phone = view.get_phone()
        password = view.encoded_password()
        department = self.get_department()
        department_id = department.id
        return {
            "username": username,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "password": password,
            "department_id": department_id,
        }

    def get_department(self):
        """Get department from user input.

        Returns:
            Department: The selected department.
        """
        department_manager = DepartmentManager()
        department_controller = DepartmentController()
        departments = department_manager.read()
        department_controller.get_table(departments=departments)
        department_id = view.select_id()
        return department_manager.get_by_id(department_id=department_id)

    def get_employee(self):
        """Get employee from user input.

        Returns:
            Employee: The selected employee.
        """
        employees = manager.read()
        self.get_table(employees=employees)
        employee_id = view.select_id()
        return manager.get_by_id(employee_id=employee_id)

    def get_user_login_department(self):
        """
        Retrieves the department ID of the logged-in user.

        Returns:
            The department ID of the logged-in user.
        """
        return self._extracted_user_info_log("department_id")

    def get_user_id_login(self):
        """
        Retrieves the ID of the logged-in user.

        Returns:
            The ID of the logged-in user.
        """
        return self._extracted_user_info_log("employee_id")

    def _extracted_user_info_log(self, info):
        """
        Extracts the specified information from the employee login file.

        Args:
            info: The information to extract from the employee login file.

        Returns:
            The extracted information.
        """
        employee_login = EmployeeLoginController()
        employee = employee_login.read_login_file()
        return employee[info]

    def get_table(self, employees: list["Employee"]):
        """
        Displays a table of employees.

        Args:
            employees (List[Employee]): A list of employee objects to display.

        Returns:
            None
        """
        table = Table(
            title="Employee", show_header=True, header_style="bold blue"
        )
        table.add_column("ID", style="dim")
        table.add_column("Username", style="bold")
        table.add_column("Email", style="bold")
        table.add_column("Phone", style="bold")
        table.add_column("Department")
        for employee in employees:
            manager_department = DepartmentManager()
            department = manager_department.get_by_id(employee.department_id)
            table.add_row(
                str(employee.id),
                f"{employee.username} {employee.last_name}",
                employee.email,
                employee.phone,
                department.name,
            )
        console.print(table)

    def get_employee_event(self, event_id):
        employee_controllers = EmployeeController()
        employee_id = employee_controllers.get_user_id_login()
        manager.create_user_event_relation(
            employee_id=employee_id, event_id=event_id
        )


class EmployeeCreateController(EmployeeController):
    """Controller for creating an employee."""

    def run(self):
        """Run the employee creation controller.

        Returns:
            EmployeeController: The employee controller.
        """
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
            return EmployeeController()


class EmployeeReadController(EmployeeController):
    """Controller for reading employees."""

    def run(self):
        """Run the employee reading controller.

        Returns:
            EmployeeController: The employee controller.
        """
        while True:
            employees = manager.read()
            self.get_table(employees=employees)
            continu = view.select_one_to_continue()
            if continu == "1":
                return EmployeeController()


class EmployeeUpdateController(EmployeeController):
    """Controller for updating an employee."""

    def run(self):
        """Run the employee update controller.

        Returns:
            EmployeeController: The employee controller.
        """
        employee = self.get_employee()
        try:
            if manager.get_by_id(employee_id=employee.id):
                employee_data = self.get_data()
                manager.update(employee_id=employee.id, **employee_data)
                view.success_update()
            else:
                view.error_not_found()

        except Exception as e:
            logging.exception(f"Unexpected error during employee update: {e}")
        finally:
            return EmployeeController()


class EmployeeDeleteController(EmployeeController):
    """Controller for deleting an employee."""

    def run(self):
        """Run the employee deletion controller.

        Returns:
            EmployeeController: The employee controller.
        """
        employee = self.get_employee()
        if manager.delete(employee_id=employee.id):
            view.success_delete()
        else:
            view.not_found()
        return EmployeeController()


class EmployeeLoginController(EmployeeController):
    """Controller for employee login."""

    def run(self):
        """Run the employee login controller.

        Returns:
            home_controllers.HomeController or None: The home controller if
            login is successful, None otherwise.
        """
        token = self.search_token()

        if token != "":
            return home_controllers.HomeController()
        max_attempts = 3

        for _ in range(max_attempts):
            view.display_title(title="Login")
            username = view.get_username()
            if employee := manager.get_by_username(username=username):
                password_hash = employee.password
                if view.test_decode_password(password_hash=password_hash):
                    data = self.get_data_log(username=username)

                    for key, value in data.items():
                        self.write_login_file(key=key, value=value)
                    return home_controllers.HomeController()
            view.error_not_found()
        return None

    def write_login_file(self, key, value):
        """Write login data to a file.

        Args:
            key: The key to write.
            value: The value to write.
        """
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
        """Read login data from a file.

        Returns:
            dict: The login data.
        """
        if not os.path.exists(FILEPATH):
            return {}

        try:
            with open(FILEPATH, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            return {}
        return data

    def login_file(self):
        """Read login file.

        Returns:
            int: The employee ID from the login file.
        """
        with open(FILEPATH) as f:
            return json.load(f)["employee_id"]

    def create_token(self, username):
        """Create a token for the given username.

        Args:
            username: The username to create the token for.

        Returns:
            str: The created token.
        """
        return pbkdf2_sha256.using(salt_size=64).hash(username)

    def search_token(self):
        """Search for a token in the login file.

        Returns:
            str: The found token.
        """
        with open(FILEPATH) as f:
            return json.load(f)["token"]

    def get_data_log(self, username):
        """Get login data for the given username.

        Args:
            username: The username to get the login data for.

        Returns:
            dict: The login data.
        """
        employee = manager.get_by_username(username=username)
        department_id = employee.department_id
        employee_id = employee.id
        token = self.create_token(username=username)
        return {
            "employee_id": employee_id,
            "department_id": department_id,
            "token": token,
        }


class EmployeeLogoutController(EmployeeController):
    """Controller for employee logout."""

    def run(self):
        """Run the employee logout controller.

        Returns:
            None
        """
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
