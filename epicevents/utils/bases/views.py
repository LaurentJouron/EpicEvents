from ..contants import SHORT_SLEEP
import re
import time
import typer

from datetime import datetime
from rich.console import Console


class BaseManageConsole:
    def _clean_console(self) -> None:
        self.console.clear()

    def _display_title(self, title: str) -> None:
        self.console.rule(f"[bold blue]{title}")


class BaseSuccessView(BaseManageConsole):
    def _success_message(self, var: str) -> None:
        self.console.print(f"\n✔️ {var}", style="bold green", justify="left")
        time.sleep(SHORT_SLEEP)
        self._clean_console()

    def _success_creating(self) -> None:
        self._success_message(" Creating successfully ")

    def _success_updated(self) -> None:
        self._success_message(" Updated successfully ")

    def _success_delete(self) -> None:
        self._success_message(" Deleted successfully ")


class BaseErrorView(BaseManageConsole):
    def __message_error(self, var: str) -> None:
        self.console.print(f"\n⛔️ {var}", style="bold red", justify="left")
        time.sleep(SHORT_SLEEP)
        self._clean_console()

    def _not_found(self) -> None:
        self.__message_error(" Not found.")

    def _invalid_id(self) -> None:
        self.__message_error(" Is no valid.")

    def _exist_error(self) -> None:
        self.__message_error(" Is already registered.")

    def _delete_aborted(self) -> None:
        self.__message_error(" Not deleting.")

    def _menu_error(self, item: str) -> None:
        self.__message_error(f" {item} is not in menu.")

    def _must_be_provided(self) -> None:
        self.__message_error(" This element must be filled in.")

    def _not_have_right(self) -> None:
        self.__message_error(" You do not have the rights")

    def _format_date_error(self):
        self.__message_error("Please use ddmmaaaa format.")

    def _earlier_invalid_date(self):
        self.__message_error("Please enter a date not earlier than today.")

    def _invalid_end_date(self):
        self.__message_error("End date should not be earlier than start date.")


class BaseAnswerView(BaseSuccessView, BaseErrorView):
    def __get_answer(self, prompt: str) -> str:
        while True:
            item = typer.prompt(f"\nPlease enter the {prompt} ").strip()
            if not item:
                self._must_be_provided()
                time.sleep(SHORT_SLEEP)
            else:
                # self._clean_console()
                return item

    def _get_username(self) -> str:
        return self.__get_answer(prompt="username").capitalize()

    def _get_lastname(self) -> str:
        return self.__get_answer(prompt="lastname").capitalize()

    def _get_compagny_name(self) -> str:
        return self.__get_answer(prompt="compagny name").capitalize()

    def _get_name(self) -> str:
        return self.__get_answer(prompt="name").capitalize()

    def _get_email(self) -> str:
        return self.__get_answer(prompt="email").lower()

    def _get_address(self) -> str:
        return self.__get_answer(prompt="address")

    def _get_information(self) -> str:
        return self.__get_answer(prompt="information")

    def _get_phone_number(self) -> str:
        return self.__get_answer(prompt="phone number")

    def _get_password(self) -> str:
        return self.__get_answer(prompt="password").upper()

    def _select_number(self) -> str:
        return self.__get_answer(prompt="number")

    def _select_id(self) -> int:
        ident = self.__get_answer(prompt="ID")
        return int(ident)

    def _get_amount(self, type) -> int:
        return self.__get_answer(prompt=f"{type} amount")

    def _delete_item(self) -> None:
        delete = typer.confirm("Are you sure you want to delete it ?")
        if not delete:
            self._delete_aborted()
            raise typer.Abort()
        self._success_delete()


class BaseMenu(BaseManageConsole):
    def __display_menu(self, title: str, menu: dict) -> None:
        self.console.rule(f"[bold blue]{title}")
        for key in menu:
            print(f"{key} - {menu[key]} ")

    def __response_menu(self, menu: dict) -> str:
        choice = self._select_number()
        if choice in menu:
            return choice
        return self._menu_error(choice)

    def _choice_menu(self, menu_name: str, menu: dict) -> str:
        self.__display_menu(menu_name, menu=menu)
        choice = self.__response_menu(menu=menu)
        self._clean_console()
        return choice


class BaseView(BaseAnswerView, BaseMenu):
    console = Console(width=120)

    def _display_centered_title(self, title: str, stars: bool = True) -> None:
        title_str = f"\n ✨{title}✨ " if stars else title
        self.console.print(title_str, style="bold blue", justify="center")
        time.sleep(SHORT_SLEEP)
        self._clean_console()
