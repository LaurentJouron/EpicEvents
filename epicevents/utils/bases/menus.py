from ...utils.bases.views import BaseView
from ..contants import RECEPTION_COLOR


class BaseMenu(BaseView):
    def _display_menu(self, menu, menu_dict):
        self.console.rule(f"[{RECEPTION_COLOR}]{menu}")
        for key in menu_dict:
            self.console.print(f"{key} - {menu_dict[key]} ")

    def _response_menu(self, menu_dict):
        choice = self._select_number()
        if choice in menu_dict:
            return choice
        return self._message_error(choice)
