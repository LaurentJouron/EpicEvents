from epicevents.utils.bases.menus import BaseMenu


class EmployeeView(BaseMenu):
    employee_menu: dict = {
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

    def get_employee_data(self):
        username = self.__get_username()
        phone_number = self._get_int("Enter the phone number: ")
        password = self._get_string("Enter you password: ")
        return {
            "username": username,
            "phone_number": phone_number,
            "password_hash": password,
        }

    def get_one_employee(self):
        username = self.__get_username()
        return username

    def display_employee(self, employee):
        print(f"Username: {employee.username}")
        print(f"Email: {employee.email}")
        print(f"Phone Number: {employee.phone_number}")

    def display_employees(self, employees):
        for employee in employees:
            self.display_employee(employee)
            print("\n" + "=" * 30 + "\n")

    def display_menu(self, menu_dict):
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    def not_found(self):
        print("Person not found.")

    def delete_succefully(self):
        print("Employee deleted successfully.")

    def updated_succefully(self):
        print("Employee updated successfully.")
