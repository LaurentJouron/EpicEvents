"""
This file imports various view classes related to the EpicEvents application.

The imported views include HomeView, ReceptionView, ExitView, DepartmentView, EmployeeView, ClientView, EventView, and ContractView.
These views are responsible for displaying information and interacting with the user interface of the application.
"""

from .home_views import HomeView, ReceptionView, ExitView  # noqa: F401
from .department_views import DepartmentView  # noqa: F401
from .employee_views import EmployeeView  # noqa: F401
from .client_views import ClientView  # noqa: F401
from .event_views import EventView  # noqa: F401
from .contract_views import ContractView  # noqa: F401
