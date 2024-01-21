from ..utils.bases.views import BaseView
from ..utils.contants import MENU


class EventView(BaseView):
    def menu_choice(self):
        return self._choice_menu("Event menu", menu=MENU)

    def display_title(self):
        return self._display_title("Create events")

    def get_name(self):
        return self._get_name()

    def get_date(self, type):
        return self._get_date(type=type)

    def get_address(self):
        return self._get_address()

    def get_number(self):
        return self._select_number()

    def get_notes(self):
        return self._get_information()

    def message_error(self, var):
        return self._message_error(var)

    def success_message(self):
        return self._success_message()

    def success_update(self):
        return self._success_updated()

    def select_id(self):
        return self._select_id()

    def not_found(self):
        self._not_found()

    def exist_error(self, var):
        return super()._exist_error(var)
