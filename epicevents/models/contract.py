from ..database import Model, Session

from datetime import date
from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.session import make_transient


class ContractManager:
    """
    Manages the CRUD operations for contracts.

    Provides methods to create, read, update, and delete contract records.
    """

    # CRUD
    def create(self, **kwargs):
        """
        Creates a new contract record.

        Args:
            **kwargs: Keyword arguments for the contract attributes.
        """
        with Session() as session:
            with session.begin():
                new_contract = Contract(
                    name=kwargs["name"],
                    total_amount=kwargs["total_amount"],
                    pending_amount=kwargs["pending_amount"],
                    creation_date=date.today(),
                    status=kwargs["status"],
                    employee_id=kwargs["employee_id"],
                )
                session.add(new_contract)

    def read(self):
        """
        Retrieves all contract records.

        Returns:
            List[Contract]: A list of all contract records.
        """
        with Session() as session:
            with session.begin():
                contracts = session.query(Contract).all()
                for contract in contracts:
                    session.expunge(contract)
                    make_transient(contract)
                return contracts

    def update(self, contract_id, **kwargs):
        """
        Updates an existing contract record.

        Args:
            contract_id: The ID of the contract to update.
            **kwargs: Keyword arguments for the contract attributes to update.
        """
        with Session() as session:
            with session.begin():
                if contract := session.query(Contract).get(contract_id):
                    if kwargs["name"] not in [contract.name, ""]:
                        contract.name = kwargs["name"]
                    if kwargs["total_amount"] not in [
                        contract.total_amount,
                        "",
                    ]:
                        contract.total_amount = kwargs["total_amount"]
                    if kwargs["pending_amount"] not in [
                        contract.pending_amount,
                        "",
                    ]:
                        contract.pending_amount = kwargs["pending_amount"]
                    if kwargs["employee_id"] not in [contract.employee_id, ""]:
                        contract.employee_id = kwargs["employee_id"]

    def delete(self, contract_id):
        """
        Deletes a contract record.

        Args:
            contract_id: The ID of the contract to delete.

        Returns:
            bool: True if the contract record was deleted, False otherwise.
        """
        with Session() as session:
            with session.begin():
                if contract := session.query(Contract).get(contract_id):
                    session.delete(contract)
                    return True
                else:
                    return False

    # REQUESTS
    def get_by_id(self, contract_id):
        """
        Retrieves a contract record by ID.

        Args:
            contract_id: The ID of the contract to retrieve.

        Returns:
            Contract: The contract record with the specified ID.
        """
        with Session() as session:
            with session.begin():
                if contract := (
                    session.query(Contract)
                    .filter(Contract.id == contract_id)
                    .first()
                ):
                    session.expunge(contract)
                    make_transient(contract)
                return contract


# MODELS
class Contract(Model):
    """
    Represents a contract.

    Attributes:
        id (int): The ID of the contract.
        name (str): The name of the contract.
        total_amount (str): The total amount of the contract.
        pending_amount (str): The pending amount of the contract.
        creation_date (Date): The creation date of the contract.
        status (bool): The status of the contract.
        employee_id (int): The ID of the employee associated with the contract.
        employee (Employee): The employee associated with the contract.
        event (Event): The event associated with the contract.
    """

    __tablename__ = "contract"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    total_amount: Mapped[str] = mapped_column(String(50))
    pending_amount: Mapped[str] = mapped_column(String(50))
    creation_date: Mapped[Date] = mapped_column(Date)
    status: Mapped[bool] = mapped_column(default=False)

    employee_id: Mapped[int] = mapped_column(ForeignKey("employee.id"))
    employee: Mapped["Employee"] = relationship(back_populates="gestion")

    event: Mapped["Event"] = relationship(back_populates="contract")
