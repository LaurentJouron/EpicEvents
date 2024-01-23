from ..utils.bases.views import BaseView
from ..utils.contants import MENU

from rich.table import Table
from rich.console import Console

console = Console()


class ClientView(BaseView):
    # MENU
    def menu_choice(self):
        return self._choice_menu("Client menu", menu=MENU)

    # ANSWER
    def get_compagny_name(self):
        return self._get_compagny_name()

    def get_username(self):
        return self._get_username()

    def get_lastname(self):
        return self._get_lastname()

    def get_email(self):
        return self._get_email()

    def get_phone(self):
        return self._get_phone_number()

    def get_address(self):
        return self._get_address()

    def get_information(self):
        return self._get_information()

    def select_id(self):
        return self._select_id()

    # DISPLAY
    def display_title(self):
        return self._display_title("Client information")

    def display_table(self, clients):
        table = Table(
            title="Client", show_header=True, header_style="bold blue"
        )
        table.add_column("ID", style="dim")
        table.add_column("compagny", style="bold")
        table.add_column("full name", style="bold")
        table.add_column("email", style="bold")
        table.add_column("phone", style="bold")
        table.add_column("address", style="bold")
        table.add_column("information", style="bold")
        table.add_column("creation", style="bold")
        table.add_column("updating", style="bold")
        table.add_column("commercial_id", style="bold")
        for client in clients:
            table.add_row(
                str(client.id),
                client.compagny_name,
                f"{client.username} {client.last_name}",
                client.email,
                client.phone,
                client.address,
                client.information,
                str(client.creation_date),
                str(client.updating_date),
                str(client.commercial_id),
            )
        console.print(table)

    # SUCCESS
    def success_creating(self):
        return self._success_creating()

    def success_update(self):
        return self._success_updated()

    def success_delete(self):
        return self._success_delete()

    # ERROR
    def error_not_have_right(self) -> str:
        return self._not_have_right()

    def error_not_found(self):
        self._not_found()
