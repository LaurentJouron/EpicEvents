from ..utils.bases.views import BaseView
from ..utils.contants import MENU

from rich.table import Table
from rich.console import Console

console = Console()


class DepartmentView(BaseView):
    """
    Represents a view for managing departments.

    This class provides methods for displaying menus, getting user input,
    displaying tables of departments, and handling success and error messages
    related to department operations.
    """

    # MENU
    def choice_menu(self):
        """Display a menu and get the user's choice.

        Args:
            self

        Returns:
            The user's choice as a string.
        """
        return self._choice_menu("Role menu", menu=MENU)

    # ANSWER
    def get_name(self):
        """Get the name from user input.

        Returns:
            The name as a string.
        """
        return self._get_name()

    def select_id(self):
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
    def display_table(self, departments):
        """
        Displays a table of departments.

        Args:
            departments (List[Department]): A list of department objects to
            display.

        Returns:
            None
        """
        table = Table(
            title="Departments", show_header=True, header_style="bold blue"
        )
        table.add_column("ID", style="dim")
        table.add_column("name", style="bold")
        for department in departments:
            table.add_row(str(department.id), department.name)
        console.print(table)

    # SUCCESS
    def success_creating(self):
        """Display a success message for creating successfully."""
        return self._success_creating()

    def success_update(self):
        """Display a success message for updating successfully."""
        return self._success_updated()

    def success_delete(self):
        """Display a success message for deleting successfully."""
        return self._success_delete()

    # ERROR
    def error_not_found(self):
        """Display an error message for not found."""
        return self._not_found()

    def error_not_have_right(self):
        """Display an error message for lack of rights."""
        return self._not_have_right()
