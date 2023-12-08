from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Client(Base):
    __tablename__ = "client"
    id = Column(Integer, primary_key=True)
    compagny_name = Column(String)
    information = Column(String)
    last_name = Column(String)
    first_name = Column(String)
    username = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(Integer, unique=True)
    creation_date = Column(Date)
    updating_date = Column(Date)
    contact_commercial = Column(String)
    address = Column(String)


engine = create_engine("sqlite:///db.sqlite")
Base.metadata.create_all(engine)
