from ..utils.bases.menus import BaseMenu
from ..utils.bases.views import BaseView


class ContractView(BaseMenu, BaseView):
    contract_menu: dict = {
        "1": "Create",
        "2": "Update",
        "3": "Get by ID",
        "4": "Get by name",
        "5": "Delete",
        "6": "All",
        "7": "Return",
    }

    def menu_choice(self):
        self._display_menu("Contract menu", menu_dict=self.contract_menu)
        return self._response_menu(menu_dict=self.contract_menu)

    def message_error(self, var):
        return self._message_error(var)

    def success_message(self):
        return self._success_message()

    def success_update(self):
        return self._success_updated()

    def not_found(self):
        self._not_found()

    def exist_error(self, var):
        return super()._exist_error(var)
