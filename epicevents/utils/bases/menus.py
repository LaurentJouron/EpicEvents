from epicevents.utils.bases.views import BaseView


class BaseMenu(BaseView):
    def _display_menu(self, menu, menu_dict):
        self.console.rule(f"[bold blue] {menu}")
        for key in menu_dict:
            self.console.print(f"{key} - {menu_dict[key]} ")
        # return self._display_left_phrase(menu_options)

    def _response_menu(self, menu_dict):
        choice = self._select_number()
        if choice in menu_dict:
            return choice
        return self._message_error(choice)
