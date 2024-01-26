from ..utils.bases.views import BaseView
from ..utils.contants import MENU

from rich.table import Table
from rich.console import Console

console = Console()


class DepartmentView(BaseView):
    # MENU
    def choice_menu(self):
        return self._choice_menu("Role menu", menu=MENU)

    # ANSWER
    def get_name(self):
        return self._get_name()

    def select_id(self):
        return self._select_id()

    # DISPLAY
    def display_table(self, departments):
        table = Table(
            title="Departments", show_header=True, header_style="bold blue"
        )
        table.add_column("ID", style="dim")
        table.add_column("name", style="bold")
        for department in departments:
            table.add_row(str(department.id), department.name)
        console.print(table)

    # SUCCESS
    def success_creating(self):
        return self._success_creating()

    def success_update(self):
        return self._success_updated()

    def success_delete(self):
        return self._success_delete()

    # ERROR
    def error_not_found(self):
        return self._not_found()

    def error_not_have_right(self):
        return self._not_have_right()
