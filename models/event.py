from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Event(Base):
    __tablename__ = "event"
    id = Column(Integer, primary_key=True)
    compagny_name = Column(String)
    client_username = Column(String)
    client_mail = Column(String)
    client_phone_number = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    contact_support = Column(String)
    address = Column(String)
    attendees = Column(Integer)
    notes = Column(String)


# Création du moteur SQLAlchemy et de la table
engine = create_engine("sqlite:///db.sqlite")
Base.metadata.create_all(engine)
