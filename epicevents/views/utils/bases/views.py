import platform
import os
from rich.console import Console


class BaseView:
    reception_color = "bold blue"
    error_color = "bold red"
    phrase_color = "bold white"
    console = Console(width=100)

    # Reception presentation
    def _display_centered_title(self, title, stars=True):
        style = self.reception_color
        justify = "center"
        if stars:
            self.console.print("✨" + title + "✨", style=style, justify=justify)
        else:
            self.console.print(title, style=style, justify=justify)

    def _display_left_phrase(self, title):
        style = self.phrase_color
        justify = "left"
        return self.console.print(title, style=style, justify=justify)

    # Success presentation
    def __success(self, prompt):
        style = self.reception_color
        justify = "left"
        self.console.print("✔️ " + prompt, style=style, justify=justify)

    def _success_message(self):
        prompt = "Success"
        self.__success(prompt)

    def _success_delete(self):
        prompt = "Deleted successfully."
        self.__success(prompt)

    def _success_updated(self):
        prompt = "Updated successfully."
        self.__success(prompt)

    # Error presentation
    def __error(self, prompt):
        style = self.error_color
        justify = "left"
        self.console.print("⛔️ " + prompt, style=style, justify=justify)

    def _message_error(self, var=""):
        if var != "":
            self.__error(f"{var} is value error.")
        else:
            self.__error("Value error.")

    def _not_found(self):
        self.__error("Not found.")

    # Answer presentation
    def __get_answer(self, prompt):
        return self.console.input(prompt)

    def _get_username(self):
        prompt = "\nPlease enter the [i][bold red]username[/][/i] ? "
        return self.__get_answer(prompt=prompt).strip().capitalize()

    def _get_lastname(self):
        prompt = "\nPlease enter the [bold red]lastname[/] ? "
        return self.__get_answer(prompt=prompt).capitalize()

    def _get_name(self):
        prompt = "\nPlease enter the [bold red]name[/] ? "
        return self.__get_answer(prompt=prompt).capitalize()

    def _get_by_id(self):
        prompt = "\nPlease enter the [bold red]ID[/] ? "
        return self.__get_answer(prompt=prompt).strip().capitalize()

    def _get_password(self):
        prompt = "\nPlease enter the [bold red]password[/] ? "
        return self.__get_answer(prompt=prompt).strip().upper()

    def _select_number(self):
        prompt = "\nPlease select [bold red]number[/] ? "
        return self.__get_answer(prompt=prompt)

    def clean_console(self):
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Linux":
            os.system("clear")
