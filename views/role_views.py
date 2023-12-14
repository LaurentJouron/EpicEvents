from utils.bases.menus import BaseMenu


class RoleView(BaseMenu):
    role_menu: dict = {
        "1": "Create",
        "2": "Modify",
        "3": "Get by ID",
        "4": "Get by name",
        "5": "Get all role",
        "6": "Return",
    }

    def display_menu(self, menu_dict):
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    def role_name(self):
        self._get_string("Enter a role: ").strip().capitalize()

    def get_by_id(self):
        self._get_int("Enter ID: ")
