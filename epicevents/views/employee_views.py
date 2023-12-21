from epicevents.utils.bases.menus import BaseMenu


class EmployeeView(BaseMenu):
    employee_menu: dict = {
        "1": "Signup",
        "2": "Get by name",
        "3": "Get by ID",
        "4": "Modify",
        "5": "Delete",
        "6": "All",
        "7": "Return",
    }

    def display_employees(self, employees):
        for employee in employees:
            self.display_employee(employee)
            print("\n" + "=" * 30 + "\n")

    def get_employee_data(self):
        username = self._get_username()
        last_name = self._get_lastname()
        email = self._get_string("Enter email: ")
        phone = self._get_string("Enter the phone number: ")
        password = self.get_password
        return {
            "username": username,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "password": password,
        }

    def get_username(self):
        return self._get_username()

    def get_password(self):
        return input("Enter password: ").strip()

    def display_employee(self, employee):
        print(f"Username: {employee.username}")
        print(f"Last name: {employee.last_name}")
        print(f"Email: {employee.email}")
        print(f"Phone Number: {employee.phone_number}")

    def display_menu(self, menu_dict):
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    def not_found(self):
        self.not_found()

    def delete_succefully(self):
        self._delete_succefully()

    def updated_succefully(self):
        self._updated_succefully()
