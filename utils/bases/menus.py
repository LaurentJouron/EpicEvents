from utils.bases.views import BaseView


class BaseMenu(BaseView):
    def _display_menu(self, menu_dict):
        menu_options = " | ".join(
            [f" {keys}. {value} " for keys, value in menu_dict.items()]
        )
        return self._star_presentation(menu_options)

    def _response_menu(self, menu_dict):
        choice = self._select_number()
        if choice in menu_dict:
            return choice
        return self._message_error(choice)
