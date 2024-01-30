from ..utils.bases.views import BaseView
from ..utils.contants import MENU

from passlib.hash import pbkdf2_sha256
from rich.table import Table
from rich.console import Console

console = Console()


class EmployeeView(BaseView):
    """
    Represents a view for managing employees.

    This class provides methods for displaying menus, getting user input,
    displaying tables of employees, handling success and error messages
    related to employee operations, and performing password-related functions.
    """

    # MENU
    def menu_choice(self) -> str:
        """Display a menu and get the user's choice.

        Returns:
            The user's choice as a string.
        """
        return self._choice_menu(menu_name="Employee menu", menu=MENU)

    # ANSWER
    def get_username(self) -> str:
        """Get the username from user input.

        Returns:
            The username as a string.
        """
        return self._get_username()

    def get_lastname(self) -> str:
        """Get the lastname from user input.

        Returns:
            The lastname as a string.
        """
        return self._get_lastname()

    def get_email(self) -> str:
        """Get the email from user input.

        Returns:
            The email as a string.
        """
        return self._get_email()

    def get_phone(self) -> str:
        """Get the phone number from user input.

        Returns:
            The phone number as a string.
        """
        return self._get_phone_number()

    def select_id(self) -> int:
        """Select an ID from user input.

        Returns:
            The selected ID as an integer.
        """
        return self._select_id()

    def select_one_to_continue(self):
        """Select a number from user input.

        Returns:
            The selected number as a string.
        """
        return self._select_one_to_continue()

    # DISPLAY
    def display_title(self, title: str):
        """Display a formatted title in the console.

        Args:
            title: The title to display.

        """
        return self._display_title(title=title)

    def display_table(self, employees: list["Employee"]):
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
        table.add_column("username", style="bold")
        table.add_column("email", style="bold")
        table.add_column("phone", style="bold")
        table.add_column("department_id")
        for employee in employees:
            table.add_row(
                str(employee.id),
                f"{employee.username} {employee.last_name}",
                employee.email,
                employee.phone,
                str(employee.department_id) if employee.department_id else "",
            )
        console.print(table)

    # SUCCESS
    def success_creating(self) -> str:
        """Display a success message for creating successfully."""
        return self._success_creating()

    def success_update(self):
        """Display a success message for updating successfully."""
        return self._success_updated()

    def success_delete(self):
        """Display a success message for deleting successfully."""
        return self._success_delete()

    # ERROR
    def error_not_have_right(self) -> str:
        """Display an error message for lack of rights."""
        return self._not_have_right()

    def error_not_found(self):
        """Display an error message for not found."""
        return self._not_found()

    # PASSWORD FUNCTIONS
    def encoded_password(self) -> str:
        """
        Encodes a password using PBKDF2 SHA256 algorithm.

        Args:
            self

        Returns:
            str: The encoded password.
        """
        password = self._get_password()
        return pbkdf2_sha256.using(salt_size=64).hash(password)

    def test_decode_password(self, password_hash: str) -> bool:
        """
        Tests if a password matches a given password hash.

        Args:
            self
            password_hash (str): The password hash to compare against.

        Returns:
            bool: True if the password matches the hash, False otherwise.
        """
        password = self._get_password()
        return pbkdf2_sha256.verify(password, password_hash)
