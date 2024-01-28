from ..database import Model, Session

from datetime import date
from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.session import make_transient


class ContractManager:
    # CRUD
    def create(self, **kwargs):
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
        with Session() as session:
            with session.begin():
                contracts = session.query(Contract).all()
                for contract in contracts:
                    session.expunge(contract)
                    make_transient(contract)
                return contracts

    def update(self, contract_id, **kwargs):
        with Session() as session:
            with session.begin():
                if contract := session.query(Contract).get(contract_id):
                    if kwargs["name"] != contract.name:
                        contract.name = kwargs["name"]
                    if kwargs["total_amount"] != contract.total_amount:
                        contract.total_amount = kwargs["total_amount"]
                    if kwargs["pending_amount"] != contract.pending_amount:
                        contract.pending_amount = kwargs["pending_amount"]
                    if kwargs["employee_id"] != contract.employee_id:
                        contract.employee_id = kwargs["employee_id"]

    def delete(self, contract_id):
        with Session() as session:
            with session.begin():
                if contract := session.query(Contract).get(contract_id):
                    session.delete(contract)
                    return True
                else:
                    return False

    # REQUESTS
    def get_by_id(self, contract_id):
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
