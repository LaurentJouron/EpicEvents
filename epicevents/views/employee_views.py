from passlib.hash import pbkdf2_sha256
from rich.table import Table
from rich.console import Console
from ..utils.bases.menus import BaseMenu
from ..utils.bases.views import BaseView
from ..utils.contants import RECEPTION_COLOR, BOLD, DIM

console = Console()


class EmployeeView(BaseMenu, BaseView):
    employee_menu: dict = {
        "1": "Create",
        "2": "Update",
        "3": "Get username by ID",
        "4": "Get ID by username",
        "5": "Delete",
        "6": "All",
        "7": "Return",
        "8": "Get password by username",
    }

    def menu_choice(self):
        self._display_menu("Employee menu", menu_dict=self.employee_menu)
        return self._response_menu(menu_dict=self.employee_menu)

    def display_employees(self, employees):
        for employee in employees:
            self.display_employee(employee)
            print("\n" + "=" * 30 + "\n")

    def get_employee_data(self):
        username = self._get_username()
        last_name = self._get_lastname()
        email = self._get_email()
        phone = self._get_phone_number()
        password = self._get_password()
        encoded_password = self.encoded_password(password=password)
        return {
            "username": username,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "password": encoded_password,
        }

    def get_username(self):
        return self._get_username()

    def display_employee_table(self, employees):
        self._display_menu("Employee table", menu_dict="")
        table = Table(
            title="Employee", show_header=True, header_style=RECEPTION_COLOR
        )
        table.add_column("ID", style=DIM)
        table.add_column("username", style=BOLD)
        table.add_column("last_name", style=BOLD)
        table.add_column("email", style=BOLD)
        table.add_column("phone", style=BOLD)
        for employee in employees:
            table.add_row(
                str(employee.id),
                employee.username,
                employee.last_name,
                employee.email,
                employee.phone,
            )
        console.print(table)

    def display_menu(self, menu_dict):
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    def encoded_password(self, password):
        return pbkdf2_sha256.using(salt_size=64).hash(password)

    def test_decode_password(self, password_hash):
        password = self._get_password()
        return pbkdf2_sha256.verify(password, password_hash)

    def display_employee(self, employee):
        print(f"Username: {employee.username}")
        print(f"Last name: {employee.last_name}")
        print(f"Email: {employee.email}")
        print(f"Phone Number: {employee.phone_number}")

    def not_found(self, var=""):
        self._not_found(var=var)

    def exist_error(self, var):
        return super()._exist_error(var)

    def delete_succefully(self):
        self._delete_succefully()

    def updated_succefully(self):
        self._updated_succefully()

    def success_creating(self):
        return self._success_creating()

    def clean_console(self):
        self._clean_console()

    def display_login(self):
        return self._display_title("Login")

    def display_create_employee(self):
        return self._display_title("Create employee")
