import tempfile

from rich.table import Table
from rich.console import Console

from ..utils.bases.views import BaseView
from ..utils.contants import RECEPTION_COLOR, BOLD, DIM, IDENT, NAME

console = Console()


class ClientView(BaseView):
    client_menu: dict = {
        "1": "Create",
        "2": "Update",
        "3": "Delete",
        "4": "All",
        "5": "Return",
    }

    def menu_choice(self):
        return self._choice_menu("Client menu", menu_dict=self.client_menu)

    def get_client_data(self):
        self._display_title("Client information")
        compagny_name = self._get_compagny_name()
        username = self._get_username()
        last_name = self._get_lastname()
        email = self._get_email()
        phone = self._get_phone_number()
        address = self._get_address()
        information = self._get_information()

        temp_file = tempfile.NamedTemporaryFile(mode="w", delete=False)
        with open(temp_file.name, "r") as file:
            content = file.read()
            # Recherche de la chaîne "employee_id=" dans le contenu
            index = content.find("employee_id=")
            if index != -1:
                # Extrait la partie après "employee_id="
                commercial_id = content[index + len("employee_id=") :].strip()
                print(commercial_id)
            else:
                # Initialise commercial_id avec une valeur par défaut si "EMPLOYEE_ID" n'est pas trouvé
                commercial_id = None
                print("employee_id non trouvé dans le fichier temporaire.")

        return {
            "compagny_name": compagny_name,
            "username": username,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "address": address,
            "information": information,
            "commercial_id": commercial_id,
        }

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
        # table.add_column("creation_date", style=BOLD)
        # table.add_column("updating_date", style=BOLD)
        # table.add_column("commercial_id", style=BOLD)
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
                # client.creation_date,
                # client.updating_date,
                # client.commercial_id,
            )
        console.print(table)

    def get_id(self):
        self._display_title(IDENT)
        ident = self._get_id()
        return ident

    def get_name(self):
        self._display_title(NAME)
        name = self._get_name()
        return name

    def client_information(self, title):
        return self._display_left_phrase(title=title)

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

    def display_name(self, name):
        return self._display_left_phrase(title=name)

    def role_information(self, title):
        return self._display_left_phrase(title=title)

    def invalid_id(self, title):
        return self._invalid_id(title=title)

    def clean_console(self):
        self._clean_console()
