from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from EpicEvents.database import Model


class Role(Model):
    _tablename_ = "role"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return f"Role(id={self.id}, name='{self.name}')"
