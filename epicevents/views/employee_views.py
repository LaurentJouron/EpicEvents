from ..utils.bases.views import BaseView
from ..utils.contants import MENU

from passlib.hash import pbkdf2_sha256
from rich.table import Table
from rich.console import Console

console = Console()


class EmployeeView(BaseView):
    # MENU
    def menu_choice(self) -> str:
        return self._choice_menu("Employee menu", menu=MENU)

    # ANSWER
    def get_username(self) -> str:
        return self._get_username()

    def get_lastname(self) -> str:
        return self._get_lastname()

    def get_email(self) -> str:
        return self._get_email()

    def get_phone(self) -> str:
        return self._get_phone_number()

    def select_id(self) -> int:
        return self._select_id()

    # DISPLAY
    def display_title(self, title: str):
        return self._display_title(title)

    def display_table(self, employees: list["Employee"]):
        table = Table(
            title="Employee", show_header=True, header_style="bold blue"
        )
        table.add_column("ID", style="dim")
        table.add_column("username", style="bold")
        table.add_column("email", style="bold")
        table.add_column("phone", style="bold")
        table.add_column("role_id")
        for employee in employees:
            table.add_row(
                str(employee.id),
                f"{employee.username} {employee.last_name}",
                employee.email,
                employee.phone,
                str(employee.role_id) if employee.role_id else "",
            )
        console.print(table)

    # SUCCESS
    def success_delete(self):
        return self._success_delete()

    def success_update(self):
        return self._success_updated()

    def success_creating(self) -> str:
        return self._success_creating()

    # ERROR
    def error_not_have_right(self) -> str:
        return self._not_have_right()

    def error_not_found(self):
        return self._not_found()

    # PASSWORD FUNCTIONS
    def encoded_password(self) -> str:
        password = self._get_password()
        return pbkdf2_sha256.using(salt_size=64).hash(password)

    def test_decode_password(self, password_hash: str) -> bool:
        password = self._get_password()
        return pbkdf2_sha256.verify(password, password_hash)
