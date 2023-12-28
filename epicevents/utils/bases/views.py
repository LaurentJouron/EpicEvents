from rich.console import Console
from ..contants import SIZE_LINE


class BaseView:
    RECEPTION_COLOR = "bold blue"
    ERROR_COLOR = "bold magenta"
    PHRASE_COLOR = "bold white"
    SUCCESS_COLOR = "bold green"
    CENTER = "center"
    LEFT = "left"
    console = Console(width=SIZE_LINE)

    # Reception presentation
    def _display_centered_title(self, title, stars=True):
        title_str = f"✨{title}✨" if stars else title
        self.console.print(
            title_str, style=self.RECEPTION_COLOR, justify=self.CENTER
        )

    def _display_left_phrase(self, title):
        self.console.print(title, style=self.PHRASE_COLOR, justify=self.LEFT)

    def _display_title(self, title):
        self.console.rule(f"[{self.RECEPTION_COLOR}]{title}")

    # Success presentation
    def _success_message(self, prompt="Success."):
        self.console.print(
            f"✔️ {prompt}", style=self.SUCCESS_COLOR, justify=self.LEFT
        )

    def _success_delete(self):
        self._success_message("Deleted successfully.")

    def _success_updated(self):
        self._success_message("Updated successfully.")

    # Error presentation
    def _message_error(self, var=""):
        var_msg = f"{var} is value error." if var else "Value error."
        self.console.print(
            f"⛔️ {var_msg}", style=self.ERROR_COLOR, justify=self.LEFT
        )

    def _not_found(self):
        self._message_error("Not found.")

    def _exist_error(self, var):
        self._message_error(f"{var} is already registered.")

    # Answer presentation
    def _get_answer(self, prompt):
        return self.console.input(prompt)

    def _get_answer_item(self, item):
        prompt = (
            f"\nPlease enter the [i][{self.RECEPTION_COLOR}]{item}: [/][/i]"
        )
        return self._get_answer(prompt=prompt)

    def _get_username(self):
        return self._get_answer_item("username").strip().capitalize()

    def _get_lastname(self):
        return self._get_answer_item("lastname").capitalize()

    def _get_name(self):
        return self._get_answer_item("name").capitalize()

    def _get_email(self):
        return self._get_answer_item("email").lower()

    def _get_phone_number(self):
        return self._get_answer_item("phone number")

    def _get_id(self):
        return self._get_answer_item("ID").strip()

    def _get_password(self):
        return self._get_answer_item("password").strip().upper()

    def _select_number(self):
        number = self._get_answer_item("number").strip()
        self.clean_console()
        return number

    # Clean console
    def clean_console(self):
        self.console.clear()
