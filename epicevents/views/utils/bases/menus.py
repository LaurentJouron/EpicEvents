from epicevents.views.utils.bases.views import BaseView


class BaseMenu(BaseView):
    def _display_menu(self, menu, menu_dict):
        self.console.rule(f"[bold blue]{menu}")
        for key in menu_dict:
            self.console.print(f"{key} - {menu_dict[key]} ")

    def _response_menu(self, menu_dict):
        choice = self._select_number()
        for key, value in menu_dict.items():
            if value == choice:
                return key
        return self._message_error(choice)
