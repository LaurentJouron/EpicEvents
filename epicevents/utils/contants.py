"""
Constants used in the EpicEvents application.

CONFIRMATION_MENU (dict): A dictionary mapping confirmation menu options to their corresponding labels.
MENU (dict): A dictionary mapping menu options to their corresponding labels.
FILEPATH (str): The filepath for the login file.
ADMIN (int): The constant representing the admin role.
COMMERCIAL (int): The constant representing the commercial role.
GESTION (int): The constant representing the gestion role.
SUPPORT (int): The constant representing the support role.
SHORT_SLEEP (int): The constant representing a short sleep duration.
LONG_SLEEP (int): The constant representing a long sleep duration.
SIZE_LINE (int): The constant representing the size of a line.
"""

CONFIRMATION_MENU: dict = {"1": "Yes", "2": "No"}
MENU: dict = {
    "1": "Create",
    "2": "Read",
    "3": "Update",
    "4": "Delete",
    "5": "Return",
}

FILEPATH = "epicevents/utils/login/login_file.json"

ADMIN: int = 0
COMMERCIAL: int = 1
GESTION: int = 2
SUPPORT: int = 3

SHORT_SLEEP: int = 1
LONG_SLEEP: int = 2

SIZE_LINE: int = 100
