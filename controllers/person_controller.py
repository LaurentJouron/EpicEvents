from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from EpicEvents import controllers as home
from models.person import Person
from views.person_views import PersonView

view = PersonView()


class PersonController:
    def __init__(self):
        # Configuration la base de données et la session
        engine = create_engine("sqlite:///db.sqlite")
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def run(self):
        while True:
            choice = view._display_menu(view.person_menu)
            if choice == "1":
                return PersonCreationController()
            elif choice == "2":
                return PersonModifyController()
            elif choice == "3":
                return PersonDeleteController()
            elif choice == "4":
                return PersonDisplayAll()
            elif choice == "5":
                return home.HomeController()


class PersonCreationController:
    def __init__(self):
        self.model = Person

    def run(self):
        person_data = view.get_person_data()
        new_person = Person(**person_data)
        new_person.register(self.session)
        return PersonController()


class PersonModifyController:
    def __init__(self):
        self.model = Person

    def run(self):
        username = view.get_one_person()
        person = (
            self.session.query(Person).filter_by(username=username).first()
        )

        if person:
            new_data = view.get_person_data()
            for key, value in new_data.items():
                setattr(person, key, value)
            self.session.commit()
            self.updated_succefully()
        else:
            self.not_found()
        return PersonController()


class PersonDeleteController:
    def __init__(self):
        self.model = Person

    def run(self):
        username = view.get_one_person()
        person = (
            self.session.query(Person).filter_by(username=username).first()
        )

        if person:
            self.session.delete(person)
            self.session.commit()
            self.delete_succefully()
        else:
            self.not_found()
        return PersonController()


class PersonDisplayAll:
    def __init__(self):
        self.model = Person

    def run(self):
        persons = self.session.query(Person).all()
        self.view.display_persons(persons)
        return PersonController()
