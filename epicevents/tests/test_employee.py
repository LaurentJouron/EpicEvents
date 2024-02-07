from epicevents.controllers.employee_controllers import EmployeeController
from epicevents.models.department import Department
from epicevents.controllers.employee_controllers import (
    EmployeeUpdateController,
)


def test_get_table(capsys, employees_fixture):
    """Test for the get_table method."""
    controller = EmployeeController()
    employees = employees_fixture["employees"]
    controller.get_table(employees)
    captured = capsys.readouterr()
    assert "Employee" in captured.out


def test_update_employee(monkeypatch, employees_fixture):
    """Test for updating an employee."""
    controller = EmployeeUpdateController()
    monkeypatch.setattr(
        "epicevents.controllers.employee_controllers.EmployeeController.get_employee",
        lambda self: employees_fixture["employees"][0],
    )
    user_input = [
        "NewUsername",
        "NewLastName",
        "newemail@example.com",
        "new phone",
        "newpassword",
        "2",
    ]
    monkeypatch.setattr("builtins.input", lambda _: user_input.pop(0))
    monkeypatch.setattr(
        "epicevents.controllers.employee_controllers.EmployeeController.get_department",
        lambda self: Department(id="2"),
    )
    next_controller = controller.run()
    assert isinstance(next_controller, EmployeeController)
