from rich.table import Table
from rich.console import Console

from epicevents.utils.bases.menus import BaseMenu
from ..utils.contants import (
    RECEPTION_COLOR,
    BOLD,
    NAME,
    ID,
    IDENT,
    DIM,
)

console = Console()


class RoleView(BaseMenu):
    role_menu: dict = {
        "1": "Create",
        "2": "Update",
        "3": "Get by ID",
        "4": "Get by name",
        "5": "Delete",
        "6": "All",
        "7": "Return",
    }

    def menu_choice(self):
        self._display_menu("Role menu", menu_dict=self.role_menu)
        return self._response_menu(menu_dict=self.role_menu)

    def get_name(self):
        self._display_title(NAME)
        name = self._get_name()
        return name

    def display_roles_table(self, roles):
        self._display_menu("Role table", menu_dict="")
        table = Table(
            title="Roles", show_header=True, header_style=RECEPTION_COLOR
        )
        table.add_column(ID, style=DIM)
        table.add_column(NAME, style=BOLD)
        for role in roles:
            table.add_row(str(role.id), role.name)
        console.print(table)

    def get_id(self):
        self._display_title(IDENT)
        ident = self._get_id()
        return ident

    def message_error(self, var):
        return self._message_error(var)

    def success_creating(self):
        return self._success_creating()

    def success_update(self):
        return self._success_updated()

    def success_delete(self):
        return self._success_delete()

    def not_found(self):
        self._not_found()

    def exist_error(self, var):
        return super()._exist_error(var)

    def role_information(self, title):
        return self._display_left_phrase(title=title)

    def invalid_id(self, title):
        return self._invalid_id(title=title)
