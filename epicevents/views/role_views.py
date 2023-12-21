from epicevents.utils.bases.menus import BaseMenu


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

    def initialise_role(self):
        return ("Gestion", "Support", "Commercial")

    def get_by_name(self):
        return self._get_by_name()

    def get_by_id(self):
        return self._get_by_id()

    def exist_error(self, var):
        print(f"'{var}' name already exists. Please enter a different name.")

    def invalid_id(self, var):
        print(f"This ID: '{var}' does not exist. Please enter a valid ID.")

    def invalid_name(self, var):
        print(f"No role found '{var}'. Please enter a valid role name.")

    def role_information(self, var):
        print(f"Current Role Information: {var}")

    def success_message(self, var):
        print(f"Role '{var}' added successfully.")

    def success_update(self, var):
        print(f"Role updated successfully. New Name: {var}")

    def not_found(self):
        self.not_found()

    def all_round(self):
        print("All Roles:")
