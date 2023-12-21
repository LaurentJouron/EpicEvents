import re

from epicevents.utils.contants import SIZE_LINE


def _get_string(var):
    """
    Collect a string input from the user.

    Args:
        prompt (str): The input prompt.
        validator (function, optional): A validation function.
        Defaults to None.

    Returns:
        str: The user's input.
    """
    pattern = r"^[a-zA-Z -àçéëêèïîôûù]+$"
    if re.match(pattern, var):
        return True
    else:
        return False


def _get_int(var):
    """
    Collect an integer input from the user.

    Args:
        prompt (str): The input prompt.
        validator (function, optional): A validation function.
        Defaults to None.

    Returns:
        int: The user's input as an integer.
    """
    return var.isdigit()


class BaseView:
    string_validator = _get_string
    integer_validator = _get_int

    def _get_string(self, prompt, validator=None):
        """
        Collect a string input from the user.

        Args:
            prompt (str): The input prompt.
            validator (function, optional): A validation function.
            Defaults to None.

        Returns:
            str: The user's input.
        """
        validator = validator or type(self).string_validator
        while True:
            answer = input(prompt).strip()
            if validator(answer):
                return answer

    def _get_int(self, prompt, validator=None):
        """
        Collect an integer input from the user.

        Args:
            prompt (str): The input prompt.
            validator (function, optional): A validation function.
            Defaults to None.

        Returns:
            int: The user's input as an integer.
        """
        validator = validator or type(self).integer_validator
        while True:
            answer = input(prompt).strip()
            if validator(answer):
                return int(answer)

    def _select_number(self):
        """
        Collect a number input from the user.

        Returns:
            str: The user's input as a string.
        """
        while True:
            try:
                answer = input("Select the menu number: ")
                return answer
            except ValueError:
                self._message_error(answer)

    def _space_presentation(self, prompt):
        """
        Display a presentation message with spaces.

        Args:
            prompt (str): The presentation message.
        """
        print(f"\n{prompt.center(SIZE_LINE, ' ')}")

    def _star_presentation(self, prompt):
        """
        Display a presentation message with stars.

        Args:
            prompt (str): The presentation message.
        """
        print(f"\n{prompt.center(SIZE_LINE, '*')}")

    def _message_error(self, var=""):
        """
        Display a value error message.

        Args:
            var (str, optional): The variable causing the error.
            Defaults to "".
        """
        if var != "":
            print(f"\n{var} is value error.")
        else:
            print("Value error.")

    def _message_success(self):
        """
        Display a success message.
        """
        print("Successfully.")

    def _delete_succefully(self):
        """
        Display a success message.
        """
        print("Deleted successfully.")

    def _updated_succefully(self):
        """
        Display a success message.
        """
        print("Updated successfully.")

    def _enter_information(self):
        """
        Display a success message.
        """
        return self._star_presentation(" Enter information ")

    def display_value_and_sentence(self, sentence, value):
        print(f"\n{sentence}: {value}")

    def display_made_your_choice(self):
        """
        Display a success message.
        """
        print(self._space_presentation(" MADE YOUR CHOICE "))

    def _not_found(self):
        """
        Display a success message.
        """
        print("Not found.")

    def _get_username(self):
        return self._get_string("Please enter username: ").capitalize()

    def _get_lastname(self):
        return self._get_string("Enter the last name: ").capitalize()

    def _get_name(self):
        return self._get_string("Enter the name: ").strip().capitalize()

    def _get_by_id(self):
        return self._get_int("Enter ID: ")
