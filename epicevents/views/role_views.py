from ..utils.bases.views import BaseView
from ..utils.contants import (
    RECEPTION_COLOR,
    BOLD,
    NAME,
    ID,
    IDENT,
    DIM,
)

from rich.table import Table
from rich.console import Console


console = Console()


class RoleView(BaseView):
    role_menu: dict = {
        "1": "Create",
        "2": "Update",
        "3": "Delete",
        "4": "All",
        "5": "Return",
    }

    def menu_choice(self):
        return self._choice_menu("Role menu", menu_dict=self.role_menu)

    def get_role_name(self):
        self._display_title(NAME)
        return self._get_name()

    def get_role_id(self):
        self._display_title(IDENT)
        return self._select_id()

    def display_roles_table(self, roles):
        self._display_title("Role table")
        table = Table(
            title="Roles", show_header=True, header_style=RECEPTION_COLOR
        )
        table.add_column(ID, style=DIM)
        table.add_column(NAME, style=BOLD)
        for role in roles:
            table.add_row(str(role.id), role.name)
        console.print(table)

    def success_creating(self):
        return self._success_creating()

    def success_update(self):
        return self._success_updated()

    def success_delete(self):
        return self._success_delete()

    def not_found(self):
        return self._not_found()
