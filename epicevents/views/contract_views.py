from ..utils.bases.views import BaseView
from ..utils.contants import MENU

from rich.table import Table
from rich.console import Console

console = Console()


class ContractView(BaseView):
    def menu_choice(self):
        return self._choice_menu("Contract menu", menu=MENU)

    def message_error(self, var):
        return self._message_error(var)

    def get_name(self):
        return self._get_name()

    def success_creating(self):
        return self._success_creating()

    def success_message(self):
        return self._success_message()

    def success_update(self):
        return self._success_updated()

    def success_delete(self):
        return self._success_delete()

    def not_found(self):
        self._not_found()

    def exist_error(self, var):
        return super()._exist_error(var)

    def select_id(self):
        return self._select_id()

    def display_title(self):
        return self._display_title("Create event")

    def get_amount(self, type):
        return self._get_amount(type=type)

    def display_table(self, contracts):
        table = Table(
            title="Contract", show_header=True, header_style="bold blue"
        )
        table.add_column("ID", style="dim")
        table.add_column("name", style="bold")
        table.add_column("total_amount", style="bold")
        table.add_column("outstanding_amount", style="bold")
        table.add_column("creation_date", style="bold")
        table.add_column("status", style="bold")
        table.add_column("gestion_id", style="bold")
        # table.add_column("event_id", style="bold")
        for contract in contracts:
            table.add_row(
                str(contract.id),
                contract.name,
                contract.total_amount,
                contract.outstanding_amount,
                str(contract.creation_date),
                str(contract.status),
                str(contract.gestion_id),
                # str(contract.event_id),
            )
        console.print(table)
