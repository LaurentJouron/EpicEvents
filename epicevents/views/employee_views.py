from passlib.hash import pbkdf2_sha256
from rich.table import Table
from rich.console import Console
from ..utils.bases.views import BaseView

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

    def get_username(self):
        return self._get_username()

    def get_lastname(self):
        return self._get_lastname()

    def get_email(self):
        return self._get_email()

    def get_phone_number(self):
        return self._get_phone_number()

    def encoded_password(self):
        password = self._get_password()
        return pbkdf2_sha256.using(salt_size=64).hash(password)

    def select_id(self):
        return self._select_id

    def display_employee_table(self, employees):
        self._display_title("Employee table")
        table = Table(
            title="Employee", show_header=True, header_style="bold blue"
        )
        table.add_column("ID", style="dim")
        table.add_column("username", style="bold")
        table.add_column("last_name", style="bold")
        table.add_column("email", style="bold")
        table.add_column("phone", style="bold")
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

    def test_decode_password(self, password_hash):
        password = self._get_password()
        return pbkdf2_sha256.verify(password, password_hash)

    def get_employee_id(self):
        self._display_title("ident")
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


class EmployeeCommercialView(EmployeeView):
    ...


class EmployeeGestionView(EmployeeView):
    ...


class EmployeeSupportView(EmployeeView):
    ...
