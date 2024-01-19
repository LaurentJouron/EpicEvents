from ..database import Model, Session

from datetime import date
from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.session import make_transient


class ContractManager:
    def create_contract(self, **kwargs):
        with Session() as session:
            with session.begin():
                new_contract = Contract(
                    name=kwargs["name"],
                    total_amount=kwargs["total_amount"],
                    outstanding_amount=kwargs["outstanding_amount"],
                    creation_date=date.today(),
                    status=kwargs["status"],
                    gestion_id=kwargs["gestion_id"],
                    # event_id=kwargs["event_id"],
                )
                session.add(new_contract)

    def update(self, contract_id, **kwargs):
        with Session() as session:
            with session.begin():
                contract = session.query(Contract).get(contract_id)
                if contract:
                    if kwargs["name"] != contract.name:
                        contract.name = kwargs["name"]
                    if kwargs["total_amount"] != contract.total_amount:
                        contract.total_amount = kwargs["total_amount"]
                    if (
                        kwargs["outstanding_amount"]
                        != contract.outstanding_amount
                    ):
                        contract.outstanding_amount = kwargs[
                            "outstanding_amount"
                        ]
                    # if kwargs["creation_date"] != contract.creation_date:
                    #     contract.creation_date = kwargs["creation_date"]
                    if kwargs["gestion_id"] != contract.gestion_id:
                        contract.gestion_id = kwargs["gestion_id"]
                    # if kwargs["event_id"] != contract.event_id:
                    #     contract.event_id = kwargs["event_id"]

    def get_by_id(self, contract_id):
        with Session() as session:
            with session.begin():
                return (
                    session.query(Contract)
                    .filter(Contract.id == contract_id)
                    .first()
                )

    def get_all_contract(self):
        with Session() as session:
            with session.begin():
                contracts = session.query(Contract).all()
                for contract in contracts:
                    session.expunge(contract)
                    make_transient(contract)
                return contracts

    def delete_contract(self, contract_id):
        with Session() as session:
            with session.begin():
                contract = session.query(Contract).get(contract_id)
                if contract:
                    session.delete(contract)
                    return True
                else:
                    return False


class Contract(Model):
    __tablename__ = "contract"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    total_amount: Mapped[str] = mapped_column(String(50))
    outstanding_amount: Mapped[str] = mapped_column(String(50))
    creation_date: Mapped[Date] = mapped_column(Date)
    status: Mapped[bool] = mapped_column(default=False)

    gestion_id: Mapped[int] = mapped_column(ForeignKey("employee.id"))
    gestion: Mapped["Employee"] = relationship(back_populates="gestion")

    event: Mapped["Event"] = relationship(back_populates="contract")
