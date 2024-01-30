from ..utils.bases.views import BaseView
from ..utils.contants import MENU

from rich.table import Table
from rich.console import Console

console = Console()


class ContractView(BaseView):
    # MENU
    def menu_choice(self):
        """Display a menu and get the user's choice.

        Args:
            self

        Returns:
            The user's choice as a string.
        """
        return self._choice_menu(menu_name="Contract menu", menu=MENU)

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

    # DISPLAY
    def display_title(self, title):
        """Display a formatted title in the console.

        Args:
            title: The title to display.

        """
        return self._display_title(title=title)

    def get_amount(self, type):
        """Get the amount for the given type from user input.

        Args:
            type: The type of amount.

        Returns:
            The amount as an integer.
        """
        return self._get_amount(type=type)

    def display_table(self, contracts):
        """
        Displays a table of contracts.

        Args:
            contracts (List[Contracts]): A list of contracts objects to
            display.

        Returns:
            None
        """
        table = Table(
            title="Contract", show_header=True, header_style="bold blue"
        )
        table.add_column("ID", style="dim")
        table.add_column("name", style="bold")
        table.add_column("total amount", style="bold")
        table.add_column("pending amount", style="bold")
        table.add_column("creation date", style="bold")
        table.add_column("status", style="bold")
        table.add_column("employee_id", style="bold")
        for contract in contracts:
            table.add_row(
                str(contract.id),
                contract.name,
                contract.total_amount,
                contract.pending_amount,
                str(contract.creation_date),
                str(contract.status),
                str(contract.employee_id),
            )
        console.print(table)

    def select_one_to_continue(self):
        """Select a number from user input.

        Returns:
            The selected number as a string.
        """
        return self._select_one_to_continue()

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
    def error_not_have_right(self) -> str:
        """Display an error message for lack of rights."""
        return self._not_have_right()

    def not_found(self):
        """Display an error message for not found."""
        self._not_found()

    def exist_error(self, var):
        """Display an error message for already registered."""
        return super()._exist_error(var)
