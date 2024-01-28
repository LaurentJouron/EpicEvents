from ..utils.bases.views import BaseView
from ..utils.contants import CONFIRMATION_MENU

epic_events = "EpicEvents"


class ReceptionView(BaseView):
    """
    Represents the reception view of the application.

    Provides methods to display a welcome message and instructions to the user.

    Args:
        self

    Returns:
        None
    """

    def welcome(self):
        """
        Displays a welcome message to the user.

        Args:
            self

        Returns:
            None
        """
        self._clean_console()
        welcome = f" Welcome to {epic_events} "
        self._display_centered_title(welcome)

    def follow_instructions(self):
        """
        Displays instructions to the user.

        Args:
            self

        Returns:
            None
        """
        instructions = "\nFollow the instructions below "
        self._display_centered_title(instructions, stars=False)


class HomeView(BaseView):
    """
    Represents the home view of the application.

    Provides methods to display the home menu and handle user choices.

    Args:
        self

    Returns:
        None
    """

    home_menu: dict = {
        "1": "Employee",
        "2": "Client",
        "3": "Event",
        "4": "Contract",
        "5": "Department",
        "6": "Exit",
    }

    def choice_menu(self):
        """
        Displays the home menu and prompts the user to make a choice.

        Args:
            self

        Returns:
            The user's choice as a string
        """
        return self._choice_menu("Home menu", menu=self.home_menu)

    def error_not_have_right(self) -> str:
        """
        Displays an error message when the user does not have the right
        permissions.

        Args:
            self

        Returns:
            The error message as a string
        """
        return self._not_have_right()


class ExitView(BaseView):
    """
    Represents the exit view of the application.

    Provides methods to display an exit message and handle user choices.

    Args:
        self

    Returns:
        None
    """

    def exit_program(self):
        """
        Displays an exit message to the user.

        Args:
            self

        Returns:
            None
        """
        exiting = f" EXIT {epic_events} "
        self.console.print(exiting, style="bold blue", justify="center")

    def good_by(self):
        """
        Displays a goodbye message to the user.

        Args:
            self

        Returns:
            None
        """
        phrase = f"Goodbye! Thank you for using {epic_events}"
        self._display_centered_title(title=phrase, stars=False)

    def choice_menu(self):
        """
        Displays a confirmation menu for exiting and prompts the user
        to make a choice.

        Args:
            self

        Returns:
            The user's choice as a string
        """
        return self._choice_menu("Confirm exiting", menu=CONFIRMATION_MENU)
