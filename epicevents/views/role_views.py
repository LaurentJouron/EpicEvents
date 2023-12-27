from epicevents.utils.bases.menus import BaseMenu


class RoleView(BaseMenu):
    role_menu: dict = {
        "1": "Create",
        "2": "Update",
        "3": "Get by ID",
        "4": "Get by name",
        "5": "Get all role",
        "6": "Return",
    }

    def display_menu(self):
        self._display_menu("Role menu", menu_dict=self.role_menu)
        return self._response_menu(menu_dict=self.role_menu)

    def get_name(self):
        return self._get_name()

    def get_id(self):
        return self._get_id()

    def message_error(self, var):
        return self._message_error(var)

    def role_information(self, var):
        print(f"Current Role Information: {var}")

    def success_message(self):
        return self._success_message()

    def success_update(self):
        return self._success_updated()

    def not_found(self):
        self._not_found()

    def exist_error(self, var):
        return super()._exist_error(var)
