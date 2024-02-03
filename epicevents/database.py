import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# database connection
engine = create_engine(os.getenv("DATABASE_URL"))

Session = sessionmaker(engine)


class Model(DeclarativeBase):
    """Base model class for database models."""

    pass
