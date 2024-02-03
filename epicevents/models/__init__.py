"""
This file imports various models and managers related to the EpicEvents application.

The imported models include Department, Employee, Client, Event, and Contract.
The imported managers include DepartmentManager, EmployeeManager, ClientManager, EventManager, and ContractManager.
These models and managers are used for data management and manipulation within the application.
"""

from .department import Department, DepartmentManager  # noqa: F401
from .employee import Employee, EmployeeManager  # noqa: F401
from .client import Client, ClientManager  # noqa: F401
from .event import Event, EventManager  # noqa: F401
from .contract import Contract, ContractManager  # noqa: F401
