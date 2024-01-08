from ..contants import (
    SIZE_LINE,
    RECEPTION_COLOR,
    ERROR_COLOR,
    PHRASE_COLOR,
    SUCCESS_COLOR,
    CENTER,
    LEFT,
)

from rich.console import Console


class BaseSuccessView:
    def _success_message(self, prompt):
        self.console.print(f"\n✔️ {prompt}", style=SUCCESS_COLOR, justify=LEFT)

    def _success_delete(self):
        self._success_message(" Deleted successfully ")

    def _success_creating(self):
        self._success_message(" Creating successfully ")

    def _success_updated(self):
        self._success_message(" Updated successfully ")


class BaseErrorView:
    def _message_error(self, var_msg=""):
        self.console.print(f"\n⛔️ {var_msg}", style=ERROR_COLOR, justify=LEFT)

    def _not_found(self, var=""):
        self._message_error(" Not found.")

    def _invalid_id(self, var=""):
        self.console.print(f" {var} is no valid.")

    def _exist_error(self, var):
        self.console.print(f" {var} is already registered.")


class BaseAnswerView:
    def _get_answer(self, prompt):
        return self.console.input(prompt)

    def _get_answer_item(self, item):
        prompt = f"\nPlease enter the [i][{RECEPTION_COLOR}]{item}: [/][/i]"
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
        return self._get_answer_item("number").strip()


class BaseView(BaseErrorView, BaseSuccessView, BaseAnswerView):
    console = Console(width=SIZE_LINE)

    # Reception presentation
    def _display_centered_title(self, title, stars=True):
        title_str = f"\n✨{title}✨" if stars else title
        self.console.print(title_str, style=RECEPTION_COLOR, justify=CENTER)

    def _display_left_phrase(self, title):
        self.console.print(title, style=PHRASE_COLOR, justify=LEFT)

    def _display_title(self, title):
        self.console.rule(f"[{RECEPTION_COLOR}]{title}")

    def _clean_console(self):
        self.console.clear()
