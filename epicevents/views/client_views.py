from rich.table import Table
from rich.console import Console
from datetime import datetime

from ..utils.bases.menus import BaseMenu
from ..utils.contants import RECEPTION_COLOR, BOLD, DIM

console = Console()


class ClientView(BaseMenu):
    client_menu: dict = {
        "1": "Create",
        "2": "Update",
        "3": "Get by ID",
        "4": "Get by Compagny name",
        "5": "Delete",
        "6": "All",
        "7": "Return",
    }

    def menu_choice(self):
        self._display_menu("Client menu", menu_dict=self.client_menu)
        return self._response_menu(menu_dict=self.client_menu)

    def get_client_data(self):
        compagny_name = self._get_answer_item("compagny name").capitalize()
        username = self._get_username()
        last_name = self._get_lastname()
        email = self._get_email()
        phone = self._get_phone_number()
        address = self._get_answer_item("address")
        information = self._get_answer_item("information")
        creation_date = datetime.now()
        return (
            compagny_name,
            username,
            last_name,
            email,
            phone,
            address,
            information,
            creation_date,
        )

    def display_client_table(self, clients):
        self._display_menu("Client table", menu_dict="")
        table = Table(
            title="Client", show_header=True, header_style=RECEPTION_COLOR
        )
        table.add_column("ID", style=DIM)
        table.add_column("compagny_name", style=BOLD)
        table.add_column("username", style=BOLD)
        table.add_column("last_name", style=BOLD)
        table.add_column("email", style=BOLD)
        table.add_column("phone", style=BOLD)
        table.add_column("address", style=BOLD)
        table.add_column("information", style=BOLD)
        table.add_column("creation_date", style=BOLD)
        table.add_column("updating_date", style=BOLD)
        table.add_column("commercial_id", style=BOLD)
        for client in clients:
            table.add_row(
                str(client.id),
                client.compagny_name,
                client.username,
                client.last_name,
                client.email,
                client.phone,
                client.address,
                client.information,
                client.creation_date,
                client.updating_date,
                client.commercial_id,
            )
        console.print(table)

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
