import string

from epicevents.utils.contants import SIZE_LINE


def _get_string(var):
    allowed_characters = string.ascii_letters + "-"
    return all(char in allowed_characters for char in var)


def _get_int(var):
    return var.isdigit()


class BaseView:
    string_validator = _get_string
    integer_validator = _get_int

    def _get_string(self, prompt, validator=None):
        validator = validator or type(self).string_validator
        while True:
            answer = input(prompt).strip()
            if validator(answer):
                return answer

    def _get_int(self, prompt, validator=None):
        validator = validator or type(self).integer_validator
        while True:
            answer = input(prompt).strip()
            if validator(answer):
                return int(answer)

    def _select_number(self):
        while True:
            try:
                answer = input("Select the menu number: ")
                return answer
            except ValueError:
                self._message_error(answer)

    def _space_presentation(self, prompt):
        print(f"\n{prompt.center(SIZE_LINE, ' ')}")

    def _star_presentation(self, prompt):
        print(f"\n{prompt.center(SIZE_LINE, '*')}")

    def _message_error(self, var=""):
        if var != "":
            print(f"\n{var} is value error.")
        else:
            print("Value error.")

    def _message_success(self):
        print("Successfully.")

    def _delete_succefully(self):
        print("Deleted successfully.")

    def _updated_succefully(self):
        print("Updated successfully.")

    def _enter_information(self):
        return self._star_presentation(" Enter information ")

    def display_value_and_sentence(self, sentence, value):
        print(f"\n{sentence}: {value}")

    def display_made_your_choice(self):
        print(self._space_presentation(" MADE YOUR CHOICE "))

    def _get_first_name(self):
        return self._get_string("Please enter first name: ").capitalize()

    def _get_last_name(self):
        return self._get_string("Enter the last name: ").capitalize()

    def _get_name(self):
        return self._get_string("Enter the name: ").capitalize()

    def _not_found(self):
        print("Not found.")

    def _get_by_name(self):
        return self._get_string("Enter a name: ").strip().capitalize()

    def _get_by_id(self):
        return self._get_int("Enter ID: ")
