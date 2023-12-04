from utils.bases.menus import BaseMenu


class PersonView(BaseMenu):
    person_menu: dict = {
        "1": "Signup",
        "2": "Modify",
        "3": "Delete",
        "5": "Quit",
    }

    def __get_username(self):
        first_name = self._get_string("Please enter first name: ").capitalize()
        last_name = self._get_string("Enter the last name: ").capitalize()
        username = f"{first_name} {last_name}"
        return username

    def get_person_data(self):
        username = self.__get_username()
        role = self._get_string("Enter the role: ").capitalize()
        phone_number = self._get_int("Enter the phone number: ")

        return {
            "username": username,
            "role": role,
            "phone_number": phone_number,
        }

    def get_one_person(self):
        username = self.__get_username()
        return username

    def display_person(self, person):
        print(f"Username: {person.username}")
        print(f"Role: {person.role}")
        print(f"Email: {person.email}")
        print(f"Phone Number: {person.phone_number}")

    def display_persons(self, persons):
        for person in persons:
            self.display_person(person)
            print("\n" + "=" * 30 + "\n")

    def not_found(self):
        print("Person not found.")

    def delete_succefully(self):
        print("Person deleted successfully.")

    def updated_succefully(self):
        print("Person updated successfully.")
