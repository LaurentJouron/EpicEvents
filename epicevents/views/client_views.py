from ..utils.bases.views import BaseView
from ..utils.contants import MENU

from rich.console import Console

console = Console()


class ClientView(BaseView):
    # MENU
    def menu_choice(self):
        """Display a menu and get the user's choice.

        Returns:
            The user's choice as a string.
        """
        return self._choice_menu(menu_name="Client menu", menu=MENU)

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

    def select_one_to_continue(self):
        """Select a number from user input.

        Returns:
            The selected number as a string.
        """
        return self._select_one_to_continue()

    # DISPLAY
    def display_title(self):
        """Display a formatted title in the console.

        Args:
            title: The title to display.
        """
        return self._display_title(title="Client information")

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
