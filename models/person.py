# models.py
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from passlib.hash import bcrypt

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(String, nullable=False)
    phone_number = Column(Integer, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    logged_in = Column(Boolean)

    def __init__(self, username, email, phone_number, password):
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.password_hash = self._hash_password(password)
        self.logged_in = False

    def _hash_password(self, password):
        # Utilisation de passlib pour hacher le mot de passe
        return bcrypt.hash(password)

    def verify_password(self, password):
        # Vérifie que le mot de passe correspond au hachage
        return bcrypt.verify(password, self.password_hash)

    def register(self, session):
        try:
            session.add(self)
            session.commit()
            print(f"Inscription réussie pour {self.username}.")
        except IntegrityError as e:
            session.rollback()
            print(f"Erreur lors de l'inscription : {e.orig}")


# Création du moteur SQLAlchemy et de la table
engine = create_engine("sqlite:///db.sqlite")
Base.metadata.create_all(engine)
