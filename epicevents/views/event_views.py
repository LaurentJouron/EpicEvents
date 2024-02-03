from ..utils.bases.views import BaseView
from ..utils.contants import MENU

from datetime import datetime
from rich.console import Console


console = Console()


class EventView(BaseView):
    # MENU
    def menu_choice(self):
        """Display a menu and get the user's choice.

        Returns:
            The user's choice as a string.
        """
        return self._choice_menu(menu_name="Event menu", menu=MENU)

    # /END_MENU

    # ANSWER
    def get_address(self):
        """Get the address from user input.

        Returns:
            The address as a string.
        """
        return self._get_address()

    def get_number(self):
        """Select a number from user input.

        Returns:
            The selected number as a string.
        """
        return self._select_number()

    def get_notes(self):
        """Get the note from user input.

        Returns:
            The note as a string.
        """
        return self._get_information()

    def select_id(self):
        """Select an ID from user input.

        Returns:
            The selected ID as an integer.
        """
        return self._select_id()

    def get_date(self, item):
        """
        Returns a date object based on the input item.

        Args:
            item: The input item.

        Returns:
            A date object representing the input item.

        Raises:
            ValueError: If the input item is not in the correct date format.

        Examples:
            >>> get_date(self, "01-01-2022")
            datetime.date(2022, 1, 1)
        """
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
        """
        Returns a valid date range based on user input.

        Returns:
            A tuple containing the start date and end date of the valid date
            range.

        Examples:
            >>> get_valid_date_range(self)
            (datetime.date(2022, 1, 1), datetime.date(2022, 1, 10))
        """
        start_date = self.get_date(item="Start")
        while True:
            end_date = self.get_date(item="End")
            if end_date >= start_date:
                return start_date, end_date
            else:
                self._earlier_invalid_date()

    def select_one_to_continue(self):
        """Select a number from user input.

        Returns:
            The selected number as a string.
        """
        return self._select_one_to_continue()

    # /END_ANSWER

    # DISPLAY
    def display_title(self, title):
        """Display a formatted title in the console.

        Args:
            title: The title to display.
        """
        return self._display_title(title=title)

    # /END_DISPLAY

    # SUCCESS
    def success_update(self):
        """Display a success message for updating successfully."""
        return self._success_updated()

    def success_creating(self):
        """Display a success message for creating successfully."""
        return self._success_creating()

    # /END_SUCCESS

    # ERROR
    def error_not_found(self):
        """Display an error message for not found."""
        self._not_found()

    def error_not_have_right(self) -> str:
        """Display an error message for lack of rights."""
        return self._not_have_right()

    # /END_ERROR
