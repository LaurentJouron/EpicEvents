from sqlalchemy import create_engine, Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


# Création du moteur SQLAlchemy et de la table
engine = create_engine("sqlite:///db.sqlite")
Base.metadata.create_all(engine)
