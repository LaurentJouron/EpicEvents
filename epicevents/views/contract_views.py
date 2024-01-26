from ..utils.bases.views import BaseView
from ..utils.contants import MENU

from rich.table import Table
from rich.console import Console

console = Console()


class ContractView(BaseView):
    # MENU
    def menu_choice(self):
        return self._choice_menu("Contract menu", menu=MENU)

    # ANSWER
    def get_name(self):
        return self._get_name()

    def select_id(self):
        return self._select_id()

    # DISPLAY
    def display_title(self, title):
        return self._display_title(title=title)

    def get_amount(self, type):
        return self._get_amount(type=type)

    def display_table(self, contracts):
        table = Table(
            title="Contract", show_header=True, header_style="bold blue"
        )
        table.add_column("ID", style="dim")
        table.add_column("name", style="bold")
        table.add_column("total amount", style="bold")
        table.add_column("pending amount", style="bold")
        table.add_column("creation date", style="bold")
        table.add_column("status", style="bold")
        table.add_column("employee_id", style="bold")
        for contract in contracts:
            table.add_row(
                str(contract.id),
                contract.name,
                contract.total_amount,
                contract.pending_amount,
                str(contract.creation_date),
                str(contract.status),
                str(contract.employee_id),
            )
        console.print(table)

    # SUCCESS
    def success_creating(self):
        return self._success_creating()

    def success_message(self):
        return self._success_message()

    def success_update(self):
        return self._success_updated()

    def success_delete(self):
        return self._success_delete()

    # ERROR

    def error_not_have_right(self) -> str:
        return self._not_have_right()

    def message_error(self, var):
        return self._message_error(var)

    def not_found(self):
        self._not_found()

    def exist_error(self, var):
        return super()._exist_error(var)
