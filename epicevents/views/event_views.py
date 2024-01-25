from ..utils.bases.views import BaseView
from ..utils.contants import MENU

from datetime import datetime
from rich.table import Table
from rich.console import Console


console = Console()


class EventView(BaseView):
    # MENU
    def menu_choice(self):
        return self._choice_menu("Event menu", menu=MENU)

    # /END_MENU

    # ANSWER
    def get_name(self):
        return self._get_name()

    def get_address(self):
        return self._get_address()

    def get_number(self):
        return self._select_number()

    def get_notes(self):
        return self._get_information()

    def select_id(self):
        return self._select_id()

    def get_date(self, item):
        while True:
            date_str = self._get_date(item=item)
            try:
                date_obj = datetime.strptime(date_str, "%d-%m-%Y").date()
                if date_obj < datetime.now().date():
                    self._later_today()
                    continue
                return date_obj
            except ValueError:
                self._format_date_error()

    def get_valid_date_range(self):
        start_date = self.get_date(item="Start")
        while True:
            end_date = self.get_date(item="End")
            if end_date >= start_date:
                return start_date, end_date
            else:
                self._earlier_invalid_date()

    # /END_ANSWER

    # DISPLAY
    def display_title(self, title):
        return self._display_title(title=title)

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
        # table.add_column("commercial_id", style="bold")
        # table.add_column("support_id", style="bold")
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
                # str(event.commercial_id),
                # str(event.support_id),
            )
        console.print(table)

    # /END_DISPLAY

    # SUCCESS
    def success_message(self):
        return self._success_message()

    def success_update(self):
        return self._success_updated()

    def success_creating(self):
        return self._success_creating()

    # /END_SUCCESS

    # ERROR
    def error_not_found(self):
        self._not_found()

    def error_not_have_right(self) -> str:
        return self._not_have_right()

    # /END_ERROR
