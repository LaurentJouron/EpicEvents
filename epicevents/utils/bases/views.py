from ..contants import SHORT_SLEEP
import time
import typer

from rich.console import Console


class BaseManageConsole:
    """
    Base class for managing console operations.

    Explanation:
    This class provides common methods for managing console operations, such
    as clearing the console and displaying formatted titles.

    Methods:
    - _clean_console(): Clears the console.
    - _display_title(title): Displays a formatted title in the console.

    """

    def _clean_console(self) -> None:
        """Clear the console.

        Explanation:
        Clears the console by calling the clear method of the console object.
        """
        self.console.clear()

    def _display_title(self, title: str) -> None:
        """Display a formatted title in the console.

        Args:
            title: The title to display.

        """
        self.console.rule(f"[bold blue]{title}")


class BaseSuccessView(BaseManageConsole):
    """
    Base class for displaying success messages in the console.

    Explanation:
    This class provides methods for displaying success messages in the console,
    such as creating, updating, and deleting successfully.

    Methods:
    - _success_message(var): Displays a success message in the console.
    - _success_creating(): Displays a success message for creating successfully.
    - _success_updated(): Displays a success message for updating successfully.
    - _success_delete(): Displays a success message for deleting successfully.

    """

    def _success_message(self, var: str) -> None:
        """Display a success message in the console.

        Args:
            var: The success message to display.
        """
        self.console.print(f"\n✔️ {var}", style="bold green", justify="left")
        time.sleep(SHORT_SLEEP)
        self._clean_console()

    def _success_creating(self) -> None:
        """Display a success message for creating successfully."""
        self._success_message(" Creating successfully ")

    def _success_updated(self) -> None:
        """Display a success message for updating successfully."""
        self._success_message(" Updated successfully ")

    def _success_delete(self) -> None:
        """Display a success message for deleting successfully."""
        self._success_message(" Deleted successfully ")


class BaseErrorView(BaseManageConsole):
    """
    Base class for displaying error messages in the console.

    Explanation:
    This class provides methods for displaying error messages in the console,
    such as not found, invalid ID, already registered, and aborted deletion.

    Methods:
    - _message_error(var): Displays an error message in the console.
    - _not_found(): Displays an error message for not found.
    - _invalid_id(): Displays an error message for invalid ID.
    - _exist_error(): Displays an error message for already registered.
    - _delete_aborted(): Displays an error message for aborted deletion.
    - _later_today(): Displays an error message for end date earlier than
    start date.
    - _menu_error(item): Displays an error message for item not in menu.
    - _must_be_provided(): Displays an error message for a required element
    not filled in.
    - _not_have_right(): Displays an error message for lack of rights.
    - _format_date_error(): Displays an error message for incorrect date
    format.
    - _earlier_invalid_date(): Displays an error message for earlier or
    invalid date.

    """

    def __message_error(self, var: str) -> None:
        """Display an error message in the console.

        Args:
            var: The error message to display.
        """
        self.console.print(f"\n⛔️ {var}", style="bold red", justify="left")
        time.sleep(SHORT_SLEEP)
        self._clean_console()

    def _not_found(self) -> None:
        """Display an error message for not found."""
        self.__message_error(" Not found.")

    def _invalid_id(self) -> None:
        """Display an error message for invalid ID."""
        self.__message_error(" Is no valid.")

    def _exist_error(self) -> None:
        """Display an error message for already registered."""
        self.__message_error(" Is already registered.")

    def _delete_aborted(self) -> None:
        """Display an error message for aborted deletion."""
        self.__message_error(" Not deleting.")

    def _later_today(self):
        """Display an error message for end date earlier than start date."""
        self.__message_error("End date should not be earlier than start date.")

    def _menu_error(self, item: str) -> None:
        """Display an error message for item not in menu.

        Args:
            item: The item that is not in the menu.
        """
        self.__message_error(f" {item} is not in menu.")

    def _must_be_provided(self) -> None:
        """Display an error message for a required element not filled in."""
        self.__message_error(" This element must be filled in.")

    def _not_have_right(self) -> None:
        """Display an error message for lack of rights."""
        self.__message_error(" You do not have the rights")

    def _format_date_error(self):
        """Display an error message for incorrect date format."""
        self.__message_error("Please use the format (dd-mm-yyyy)")

    def _earlier_invalid_date(self):
        """Display an error message for earlier or invalid date."""
        self.__message_error(
            "Please enter a date later or equal to the first."
        )


class BaseAnswerView(BaseSuccessView, BaseErrorView):
    """
    Base answer view class.

    Explanation:
    This class provides common methods for displaying messages, getting user
    input, and displaying menus in the console.

    Methods:
    - _display_centered_title(title: str, stars: bool = True) -> None: Displays
    a centered title in the console.
    - _get_username() -> str: Gets the username from user input.
    - _get_lastname() -> str: Gets the lastname from user input.
    - _get_compagny_name() -> str: Gets the company name from user input.
    - _get_name() -> str: Gets the name from user input.
    - _get_email() -> str: Gets the email from user input.
    - _get_address() -> str: Gets the address from user input.
    - _get_information() -> str: Gets the information from user input.
    - _get_phone_number() -> str: Gets the phone number from user input.
    - _get_password() -> str: Gets the password from user input.
    - _select_number() -> str: Selects a number from user input.
    - _select_id() -> int: Selects an ID from user input.
    - _get_amount(type) -> int: Gets the amount for the given type from user
    input.
    - _get_date(item) -> str: Gets the date for the given item from user input.
    - _delete_item() -> None: Deletes an item.

    """

    def __get_answer(self, prompt: str) -> str:
        """Get user input for the given prompt.

        Args:
            prompt: The prompt message.

        Returns:
            The user input as a string.
        """
        while True:
            if item := typer.prompt(f"\nPlease enter the {prompt} ").strip():
                self._clean_console()
                return item
            self._must_be_provided()
            time.sleep(SHORT_SLEEP)

    def _get_username(self) -> str:
        """Get the username from user input.

        Returns:
            The username as a string.
        """
        return self.__get_answer(prompt="username").capitalize()

    def _get_lastname(self) -> str:
        """Get the lastname from user input.

        Returns:
            The lastname as a string.
        """
        return self.__get_answer(prompt="lastname").capitalize()

    def _get_compagny_name(self) -> str:
        """Get the company name from user input.

        Returns:
            The company name as a string.
        """
        return self.__get_answer(prompt="compagny name").capitalize()

    def _get_name(self) -> str:
        """Get the name from user input.

        Returns:
            The name as a string.
        """
        return self.__get_answer(prompt="name").capitalize()

    def _get_email(self) -> str:
        """Get the email from user input.

        Returns:
            The email as a string.
        """
        return self.__get_answer(prompt="email").lower()

    def _get_address(self) -> str:
        """Get the address from user input.

        Returns:
            The address as a string.
        """
        return self.__get_answer(prompt="address")

    def _get_information(self) -> str:
        """Get the information from user input.

        Returns:
            The information as a string.
        """
        return self.__get_answer(prompt="information")

    def _get_phone_number(self) -> str:
        """Get the phone number from user input.

        Returns:
            The phone number as a string.
        """
        return self.__get_answer(prompt="phone number")

    def _get_password(self) -> str:
        """Get the password from user input.

        Returns:
            The password as a string.
        """
        return self.__get_answer(prompt="password").upper()

    def _select_number(self) -> str:
        """Select a number from user input.

        Returns:
            The selected number as a string.
        """
        return self.__get_answer(prompt="number")

    def _select_one_to_continue(self) -> str:
        """Select a number 1 from user input.

        Returns:
            The selected number as a string.
        """
        return self.__get_answer(prompt="number 1 to continue")

    def _select_id(self) -> int:
        """Select an ID from user input.

        Returns:
            The selected ID as an integer.
        """
        ident = self.__get_answer(prompt="ID")
        return int(ident)

    def _get_amount(self, type) -> int:
        """Get the amount for the given type from user input.

        Args:
            type: The type of amount.

        Returns:
            The amount as an integer.
        """
        return self.__get_answer(prompt=f"{type} amount")

    def _get_date(self, item) -> str:
        """Get the date for the given item from user input.

        Args:
            item: The item for which the date is requested.

        Returns:
            The date as a string.
        """
        return self.__get_answer(prompt=f"{item} date (dd-mm-yyyy)").strip()

    def _delete_item(self) -> None:
        """Delete an item.

        Raises:
            typer.Abort: If the deletion is aborted.
        """
        delete = typer.confirm("Are you sure you want to delete it ?")
        if not delete:
            self._delete_aborted()
            raise typer.Abort()
        self._success_delete()


class BaseMenu(BaseManageConsole):
    def __display_menu(self, title: str, menu: dict) -> None:
        """Display a menu with the given title and options.

        Args:
            title: The title of the menu.
            menu: A dictionary containing the menu options.

        Returns:
            None.
        """
        self.console.rule(f"[bold blue]{title}")
        for key in menu:
            print(f"{key} - {menu[key]} ")

    def __response_menu(self, menu: dict) -> str:
        """Get the user's choice from the menu.

        Args:
            menu: A dictionary containing the menu options.

        Returns:
            The user's choice as a string.
        """
        choice = self._select_number()
        return choice if choice in menu else self._menu_error(choice)

    def _choice_menu(self, menu_name: str, menu: dict) -> str:
        """Display a menu and get the user's choice.

        Args:
            menu_name: The name of the menu.
            menu: A dictionary containing the menu options.

        Returns:
            The user's choice as a string.
        """
        self.__display_menu(menu_name, menu=menu)
        choice = self.__response_menu(menu=menu)
        self._clean_console()
        return choice


class BaseView(BaseAnswerView, BaseMenu):
    console = Console(width=120)

    def _display_centered_title(self, title: str, stars: bool = True) -> None:
        """Display a centered title.

        Args:
            title: The title to be displayed.
            stars: Whether to surround the title with stars.

        Returns:
            None.
        """
        title_str = f"\n ✨{title}✨ " if stars else title
        self.console.print(title_str, style="bold blue", justify="center")
        time.sleep(SHORT_SLEEP)
        self._clean_console()
