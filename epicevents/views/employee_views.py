from passlib.hash import pbkdf2_sha256
from rich.table import Table
from rich.console import Console
from ..utils.bases.views import BaseView
from ..utils.contants import RECEPTION_COLOR, BOLD, DIM, IDENT

console = Console()


class EmployeeView(BaseView):
    employee_menu: dict = {
        "1": "Create",
        "2": "Update",
        "3": "Delete",
        "4": "All",
        "5": "Return",
    }

    def menu_choice(self):
        return self._choice_menu("Employee menu", menu_dict=self.employee_menu)

    def get_employee_data(self):
        role_id = self._select_id()
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
            "role_id": role_id,
        }

    def get_username(self):
        return self._get_username()

    def display_employee_table(self, employees):
        self._display_title("Employee table")
        table = Table(
            title="Employee", show_header=True, header_style=RECEPTION_COLOR
        )
        table.add_column("ID", style=DIM)
        table.add_column("username", style=BOLD)
        table.add_column("last_name", style=BOLD)
        table.add_column("email", style=BOLD)
        table.add_column("phone", style=BOLD)
        table.add_column("role_id")
        for employee in employees:
            table.add_row(
                str(employee.id),
                employee.username,
                employee.last_name,
                employee.email,
                employee.phone,
                str(employee.role_id) if employee.role_id else "",
            )
        console.print(table)

    def encoded_password(self, password):
        return pbkdf2_sha256.using(salt_size=64).hash(password)

    def test_decode_password(self, password_hash):
        password = self._get_password()
        return pbkdf2_sha256.verify(password, password_hash)

    def get_employee_id(self):
        self._display_title(IDENT)
        return self._select_id()

    def not_found(self):
        self._not_found()

    def success_delete(self):
        self._success_delete()

    def success_update(self):
        self._success_updated()

    def success_creating(self):
        return self._success_creating()

    def display_login(self):
        return self._display_title("Login")

    def display_create_employee(self):
        return self._display_title("Create employee")
