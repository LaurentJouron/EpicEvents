from ..utils.bases.views import BaseView
from ..utils.contants import MENU

from rich.table import Table
from rich.console import Console

console = Console()


class EventView(BaseView):
    def menu_choice(self):
        return self._choice_menu("Event menu", menu=MENU)

    def display_title(self, title):
        return self._display_title(title=title)

    def get_name(self):
        return self._get_name()

    def get_date(self, type):
        return self._get_date(type=type)

    def get_address(self):
        return self._get_address()

    def get_number(self):
        return self._select_number()

    def get_notes(self):
        return self._get_information()

    def message_error(self, var):
        return self._message_error(var)

    def success_message(self):
        return self._success_message()

    def success_update(self):
        return self._success_updated()

    def select_id(self):
        return self._select_id()

    def not_found(self):
        self._not_found()

    def exist_error(self, var):
        return super()._exist_error(var)

    def get_amount(self, type):
        return self._get_amount(type=type)

    def display_table(self, events):
        table = Table(
            title="Events", show_header=True, header_style="bold blue"
        )
        table.add_column("ID", style="dim")
        table.add_column("name", style="bold")
        table.add_column("start_date", style="bold")
        table.add_column("end_date", style="bold")
        table.add_column("address", style="bold")
        table.add_column("attendees", style="bold")
        table.add_column("notes", style="bold")
        table.add_column("client_id", style="bold")
        table.add_column("commercial_id", style="bold")
        table.add_column("support_id", style="bold")
        for event in events:
            table.add_row(
                str(event.id),
                event.name,
                event.start_date,
                event.end_date,
                event.address,
                event.attendees,
                event.notes,
                str(event.client_id),
                str(event.commercial_id),
                str(event.support_id),
            )
        console.print(table)
