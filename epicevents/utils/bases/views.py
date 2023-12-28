import platform
import os
from rich.console import Console


class BaseView:
    reception_color = "bold blue"
    error_color = "bold magenta"
    phrase_color = "bold white"
    success_color = "bold green"
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

    def _display_title(self, title):
        self.console.rule(f"[bold blue]{title}")

    # Success presentation
    def __success(self, prompt):
        style = self.success_color
        justify = "left"
        self.console.print("✔️ " + prompt, style=style, justify=justify)

    def _success_message(self):
        self.__success("Success.")

    def _success_delete(self):
        self.__success("Deleted successfully.")

    def _success_updated(self):
        self.__success("Updated successfully.")

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

    def _exist_error(self, var):
        return self.__error(f"{var} is already registered.")

    # Answer presentation
    def __get_answer(self, prompt):
        return self.console.input(prompt)

    def _get_username(self):
        prompt = (
            f"\nPlease enter the [i][{self.reception_color}]username: [/][/i]"
        )
        return self.__get_answer(prompt=prompt).strip().capitalize()

    def _get_lastname(self):
        prompt = f"\nPlease enter the [{self.reception_color}]lastname: [/]"
        return self.__get_answer(prompt=prompt).capitalize()

    def _get_name(self):
        prompt = f"\nPlease enter the [{self.reception_color}]name: [/]"
        return self.__get_answer(prompt=prompt).capitalize()

    def _get_id(self):
        prompt = f"\nPlease enter the [{self.reception_color}]ID: [/]"
        return self.__get_answer(prompt=prompt).strip().capitalize()

    def _get_password(self):
        prompt = f"\nPlease enter the [{self.reception_color}]password: [/]"
        return self.__get_answer(prompt=prompt).strip().upper()

    def _select_number(self):
        prompt = f"\nPlease select [{self.reception_color}]number:[/] "
        number = self.__get_answer(prompt=prompt)
        self.clean_console()
        return number

    def clean_console(self):
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Linux":
            os.system("clear")
