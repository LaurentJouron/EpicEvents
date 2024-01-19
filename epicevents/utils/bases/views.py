from ..contants import SHORT_SLEEP
import time
import typer

from rich.console import Console


class BaseManageConsole:
    """
    Base class for managing the console display.
    This class provides a method to clear the console display.
    """

    def _clean_console(self) -> None:
        """Clear the console display."""
        self.console.clear()


class BaseSuccessView(BaseManageConsole):
    """
    Base class for displaying success messages.
    This class provides methods for displaying success messages,
    such as successful creation, deletion, and update.
    """

    def _success_message(self, var: str) -> None:
        """Display a success message.
        Args:
            var (str): The variable or entity related to the success message.
        """
        self.console.print(f"\n✔️ {var}", style="bold green", justify="left")
        time.sleep(SHORT_SLEEP)
        self._clean_console()

    def _success_creating(self) -> None:
        """Display a success message for successful creation."""
        self._success_message(" Creating successfully ")

    def _success_updated(self) -> None:
        """Display a success message for successful update."""
        self._success_message(" Updated successfully ")

    def _success_delete(self) -> None:
        """Display a success message for successful deletion."""
        self._success_message(" Deleted successfully ")


class BaseErrorView(BaseManageConsole):
    """
    Base class for displaying error messages.
    This class provides methods for displaying various error messages,
    such as not found, invalid ID, existence error, delete aborted, menu error,
    and must be provided.
    """

    def __message_error(self, var: str) -> None:
        """
        Display a general error message.
        Args:
            var (str): The variable or entity related to the error message.
        """
        self.console.print(f"\n⛔️ {var}", style="bold red", justify="left")
        time.sleep(SHORT_SLEEP)
        self._clean_console()

    def _not_found(self) -> None:
        """Display an error message for not found."""
        self.__message_error(" Not found.")

    def _invalid_id(self) -> None:
        """Display an error message for an invalid ID."""
        self.__message_error(" Is no valid.")

    def _exist_error(self) -> None:
        """Display an error message for existence error."""
        self.__message_error(" Is already registered.")

    def _delete_aborted(self) -> None:
        """Display an error message for delete aborted."""
        self.__message_error(" Not deleting.")

    def _menu_error(self, item: str) -> None:
        """
        Display an error message for menu error.
        Args:
            item (str): The item that is not in the menu.
        """
        self.__message_error(f" {item} is not in menu.")

    def _must_be_provided(self) -> None:
        """
        Display an error message indicating that an element must be filled in.
        """
        self.__message_error(" This element must be filled in.")


class BaseAnswerView(BaseSuccessView, BaseErrorView):
    """
    Base class for handling user input and providing prompts.
    This class provides methods for getting various types of user input,
    such as username, lastname, name, email, phone number, password, number,
    ID, and handling the deletion confirmation.
    """

    def __get_answer(self, prompt: str) -> str:
        """
        Get user input for a given prompt.
        Args:
            prompt (str): The prompt message.
        Returns:
            str: User input.
        """
        return typer.prompt(f"\nPlease enter the {prompt} ")

    def __get_item(self, name: str) -> str:
        """
        Get user input for a specific item.
        Args:
            name (str): The name of the item.
        Returns:
            str: User input for the item.
        """
        while True:
            item = self.__get_answer(name).strip()
            if not item:
                self._must_be_provided()
                time.sleep(SHORT_SLEEP)
            else:
                return item

    def _get_username(self) -> str:
        """
        Get user input for a username.
        Returns:
            str: User input for the username.
        """
        return self.__get_item(name="username").capitalize()

    def _get_lastname(self) -> str:
        """
        Get user input for a lastname.
        Returns:
            str: User input for the lastname.
        """
        return self.__get_item(name="lastname").capitalize()

    def _get_compagny_name(self) -> str:
        """
        Get client input for a compagny name.
        Returns:
            str: client input for the compagny name.
        """
        return self.__get_item(name="compagny name").capitalize()

    def _get_name(self) -> str:
        """
        Get user input for a name.
        Returns:
            str: User input for the name.
        """
        return self.__get_item(name="name").capitalize()

    def _get_email(self) -> str:
        """
        Get user input for an email.
        Returns:
            str: User input for the email.
        """
        return self.__get_item(name="email").lower()

    def _get_address(self) -> str:
        """
        Get user input for an address.
        Returns:
            str: User input for the address.
        """
        return self.__get_item(name="address")

    def _get_information(self) -> str:
        """
        Get user input for an information.
        Returns:
            str: User input for the information.
        """
        return self.__get_item(name="information")

    def _get_phone_number(self) -> str:
        """
        Get user input for a phone number.
        Returns:
            str: User input for the phone number.
        """
        return self.__get_item(name="phone number")

    def _get_password(self) -> str:
        """
        Get user input for a password.
        Returns:
            str: User input for the password.
        """
        return self.__get_item(name="password").upper()

    def _select_number(self) -> str:
        """
        Get user input for a number.
        Returns:
            str: User input for the number.
        """
        return self.__get_item(name="number")

    def _select_id(self) -> int:
        """
        Get user input for an ID.
        Returns:
            int: User input for the ID.
        """
        ident = self.__get_item(name="ID")
        return int(ident)

    def _get_amount(self, type) -> int:
        """
        Get contract input for an amount.
        Returns:
            int: Contract input for the amount.
        """
        return self.__get_item(name=f"{type} amount")

    def _get_date(self, type) -> int:
        """
        Get input for an date.
        Returns:
            date: input for the date.
        """
        return self.__get_item(name=f"{type} date ('AAAA-MM-JJ')")

    def _delete_item(self) -> None:
        """Handle deletion confirmation."""
        delete = typer.confirm("Are you sure you want to delete it ?")
        if not delete:
            self._delete_aborted()
            raise typer.Abort()
        self._success_delete()


class BaseMenu:
    """
    Base class for handling menu-related operations.
    This class provides methods for displaying a menu, getting a user's
    menu choice, and handling the choice accordingly.
    """

    def __display_menu(self, title: str, menu_dict: dict) -> None:
        """
        Display a menu with a given title and dictionary of options.
        Args:
            title (str): The title of the menu.
            menu_dict (dict): A dictionary containing menu options.
        """
        self.console.rule(f"[bold blue]{title}")
        for key in menu_dict:
            print(f"{key} - {menu_dict[key]} ")

    def __response_menu(self, menu_dict: dict) -> str:
        """
        Get the user's menu choice and validate it against the menu options.
        Args:
            menu_dict (dict): A dictionary containing menu options.
        Returns:
            str: The user's valid menu choice.
        """
        choice = self._select_number()
        if choice in menu_dict:
            return choice
        return self._menu_error(choice)

    def _choice_menu(self, menu_name: str, menu_dict: dict) -> str:
        """
        Handle the user's choice in the menu.
        Args:
            menu_name (str): The name of the menu.
            menu_dict (dict): A dictionary containing menu options.
        Returns:
            str: The user's valid menu choice.
        """
        self.__display_menu(menu_name, menu_dict=menu_dict)
        return self.__response_menu(menu_dict=menu_dict)


class BaseView(BaseAnswerView, BaseMenu):
    """
    Base class for handling common view-related operations.
    This class provides methods for displaying titles, centered titles,
    and combining functionality from `BaseAnswerView` and `BaseMenu`.
    """

    console = Console(width=120)

    def _display_centered_title(self, title: str, stars: bool = True) -> None:
        """
        Display a centered title with optional stars around it.
        Args:
            title (str): The title to be displayed.
            stars (bool, optional): Whether to include stars around the title.
        """
        title_str = f"\n ✨{title}✨ " if stars else title
        self.console.print(title_str, style="bold blue", justify="center")
        time.sleep(SHORT_SLEEP)
        self._clean_console()

    def _display_title(self, title: str) -> None:
        """
        Display a title with a horizontal rule.
        Args:
            title (str): The title to be displayed.
        """
        self.console.rule(f"[bold blue]{title}")
