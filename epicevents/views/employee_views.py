import jwt
from ..utils.bases.menus import BaseMenu


class EmployeeView(BaseMenu):
    employee_menu: dict = {
        "1": "Create",
        "2": "Update",
        "3": "Get by ID",
        "4": "Get by name",
        "5": "Delete",
        "6": "All",
        "7": "Return",
    }

    def menu_choice(self):
        self._display_menu("Employee menu", menu_dict=self.employee_menu)
        return self._response_menu(menu_dict=self.employee_menu)

    def display_employees(self, employees):
        for employee in employees:
            self.display_employee(employee)
            print("\n" + "=" * 30 + "\n")

    def get_employee_data(self):
        username = self._get_username()
        last_name = self._get_lastname()
        email = self._get_email()
        phone = self._get_phone_number()
        password = self.get_password
        password_jwt = self.encoded_jwt(username=username, password=password)
        return {
            "username": username,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "password": password_jwt,
        }

    def display_menu(self, menu_dict):
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    def get_username(self):
        return self._get_username()

    def get_password(self):
        return input("Enter password: ").strip()

    def encoded_jwt(self, username, password):
        return jwt.encode(
            {"username": username, "password": password},
            "password",
            algorithm="HS256",
        )

    def decode_jwt(self, encoded_jwt):
        return jwt.decode(encoded_jwt, "password", algorithms=["HS256"])

    def test_encoded_decode(self, username, password, encoded):
        decode = self.decode_jwt(encoded_jwt=encoded)
        if username == decode["username"] and password == decode["password"]:
            return True
        else:
            self._message_error()

    def display_employee(self, employee):
        print(f"Username: {employee.username}")
        print(f"Last name: {employee.last_name}")
        print(f"Email: {employee.email}")
        print(f"Phone Number: {employee.phone_number}")

    def not_found(self):
        self.not_found()

    def delete_succefully(self):
        self._delete_succefully()

    def updated_succefully(self):
        self._updated_succefully()
