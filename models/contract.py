from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contract(Base):
    __tablename__ = "contract"
    id = Column(Integer, primary_key=True)
    client_information = Column(String)
    contact_commercial = Column(String)
    total_amount = Column(Integer)
    outstanding_amount = Column(Integer)
    creation_date = Column(Date)
    status = Column(Boolean)


# Création du moteur SQLAlchemy et de la table
engine = create_engine("sqlite:///db.sqlite")
Base.metadata.create_all(engine)
