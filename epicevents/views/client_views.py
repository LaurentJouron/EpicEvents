from ..utils.bases.views import BaseView
from ..utils.contants import MENU

from rich.table import Table
from rich.console import Console

console = Console()


class ClientView(BaseView):
    # MENU
    def menu_choice(self):
        """Display a menu and get the user's choice.

        Args:
            self

        Returns:
            The user's choice as a string.
        """
        return self._choice_menu("Client menu", menu=MENU)

    # ANSWER
    def get_compagny_name(self):
        """Get the company name from user input.

        Returns:
            The company name as a string.
        """
        return self._get_compagny_name()

    def get_username(self):
        """Get the username from user input.

        Returns:
            The username as a string.
        """
        return self._get_username()

    def get_lastname(self):
        """Get the lastname from user input.

        Returns:
            The lastname as a string.
        """
        return self._get_lastname()

    def get_email(self):
        """Get the email from user input.

        Returns:
            The email as a string.
        """
        return self._get_email()

    def get_phone(self):
        """Get the phone number from user input.

        Returns:
            The phone number as a string.
        """
        return self._get_phone_number()

    def get_address(self):
        """Get the address from user input.

        Returns:
            The address as a string.
        """
        return self._get_address()

    def get_information(self):
        """Get the information from user input.

        Returns:
            The information as a string.
        """
        return self._get_information()

    def select_id(self):
        """Select an ID from user input.

        Returns:
            The selected ID as an integer.
        """
        return self._select_id()

    # DISPLAY
    def display_title(self):
        """Display a formatted title in the console.

        Args:
            title: The title to display.

        """
        return self._display_title("Client information")

    def display_table(self, clients):
        """
        Displays a table of clients.

        Args:
            clients (List[Clients]): A list of client objects to display.

        Returns:
            None
        """
        table = Table(
            title="Client", show_header=True, header_style="bold blue"
        )
        table.add_column("ID", style="dim")
        table.add_column("compagny", style="bold")
        table.add_column("full name", style="bold")
        table.add_column("email", style="bold")
        table.add_column("phone", style="bold")
        table.add_column("address", style="bold")
        table.add_column("information", style="bold")
        table.add_column("creation", style="bold")
        table.add_column("updating", style="bold")
        table.add_column("employee_id", style="bold")
        for client in clients:
            table.add_row(
                str(client.id),
                client.compagny_name,
                f"{client.username} {client.last_name}",
                client.email,
                client.phone,
                client.address,
                client.information,
                str(client.creation_date),
                str(client.updating_date),
                str(client.employee_id),
            )
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
    def error_not_have_right(self) -> str:
        """Display an error message for lack of rights."""
        return self._not_have_right()

    def error_not_found(self):
        """Display an error message for not found."""
        self._not_found()
