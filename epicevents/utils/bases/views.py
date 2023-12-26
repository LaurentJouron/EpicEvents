from rich import print
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt


class BaseView:
    def __init__(self):
        super().__init__()
        self.console = Console()

    def _display_centered_title(self, title, stars=True):
        padding = (self.console.width - len(title)) // 2
        text = Text()
        if stars:
            text.append(" " * padding)
            text.append("✨" * 1, style="bright_blue")
            text.append(" " + title + " ", style="bold blue")
            text.append("✨" * 1, style="bright_blue")
            text.append(" " * padding)
        else:
            text.append(" " * padding)
            text.append(" " * 3 + title + " ", style="bold blue")
            text.append(" " * 3)
            text.append(" " * padding)
        self.console.print(text)

    def __display_test(prompt, style="bold white"):
        print(f"[{style}]{prompt}[/{style}]")

    def __ask_value(self, prompt, default):
        return Prompt.ask(prompt=prompt, default=default)

    def _message_error(self, var=""):
        if var != "":
            self.__display_test(f"\n{var} is value error.")
        else:
            self._value_error

    def _success_message(self):
        self.__display_test("✔️ Success.")

    def _success_delete(self):
        self.__display_test("✔️ Deleted successfully.")

    def _success_updated(self):
        self.__display_test("✔️ Updated successfully.")

    def _not_found(self):
        self.__display_test("⛔️ Not found.")

    def _value_error(self):
        self.__display_test("⛔️ Value error.")

    def _get_username(self):
        prompt = "Enter your username"
        default = "login username"
        return self.__ask_value(prompt=prompt, default=default).capitalize()

    def _get_lastname(self):
        prompt = "Enter your last name"
        default = ""
        return self.__ask_value(prompt=prompt, default=default).capitalize()

    def _get_name(self):
        prompt = "Enter name"
        default = ""
        return (
            self.__ask_value(prompt=prompt, default=default)
            .strip()
            .capitalize()
        )

    def _get_by_id(self):
        prompt = "Enter ID: "
        default = ""
        return self.__ask_value(prompt=prompt, default=default)

    def _get_password(self):
        prompt = "Please enter password: "
        default = ""
        return self.__ask_value(prompt=prompt, default=default).upper()
