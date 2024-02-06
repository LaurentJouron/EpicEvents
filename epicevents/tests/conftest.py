import pytest
from epicevents.models.client import Client
from epicevents.models.employee import Employee
from epicevents.models.contract import Contract
from epicevents.models.event import Event


@pytest.fixture
def fake_employees_fixture():
    return [
        Employee(
            id="1",
            username="Laurent",
            last_name="Jouron",
            email="laurent@jouron.com",
            phone="22 33 44 55 66",
            password="$pbkdf2-sha256$29000$6P0/p/QeY.ydMwbAGCOEkHKOsZZSCoEwJkRICWHsndN6r1WqlRKC8L435nxPSUnpXSslZKwV4pxzTknJmZNSKg$i4F8h7.mqBhPQcMM7l.Ge.g8C8UdlRnvg0HK9wNTub0",
            department_id="2",
        ),
        Employee(
            id="2",
            username="Antoine",
            last_name="Jouron",
            email="antoine@jouron.com",
            phone="55 66 33 22 55",
            password="$pbkdf2-sha256$29000$U0qpFUKIUUoJIaT0/n8PgfD.P2dM6Z0T4nyvNeZ8T8k5hzAGYMwZw5jznjPmfE.pdQ4hZMz5/39vjXEu5Rzj3A$GMRmWOitnqZYchM9e1QncujAozEUewR5p/aix23g6M8",
            department_id="3",
        ),
        Employee(
            id="3",
            username="Louis",
            last_name="Jouron",
            email="louis@jouron.com",
            phone="55 11 33 77 99",
            password="$pbkdf2-sha256$29000$R4iRMkaoNQaAEAKAUErpvTfm/N8b47w3RihFSGmN0fp/z3nvHUNozblX6l1LiXFubQ1ByPk/J.Scs1YqhXAOgQ$xBXGbXP/R7H9Le4ULM0sAFhon3zVtbiYQQLt.tFZKFA",
            department_id="1",
        ),
    ]


@pytest.fixture
def fake_clients_fixture():
    return [
        Client(
            id="1",
            compagny_name="Orange",
            username="Stephane",
            last_name="Richard",
            email="stephane@orange.com",
            phone="55 00 33 88 22",
            address="Caudréan (France)",
            information="Né le 24 Août 1961",
            creation_date="2024-01-26",
            updating_date="2024-01-26",
            employee_id="3",
        ),
        Client(
            id="4",
            compagny_name="Ubuntu",
            username="Mark",
            last_name="Shuttleworth",
            email="mark@ubuntu.com",
            phone="55 77 33 00 11",
            address="Welkom (Afrique du sud)",
            information="Né le 18 Septembre 1973",
            creation_date="2024-01-26",
            updating_date="2024-01-26",
            employee_id="6",
        ),
        Client(
            id="7",
            compagny_name="Python",
            username="Guido",
            last_name="Van rossum",
            email="guido@python.com",
            phone="33 77 11 00 44",
            address="Harlem (Pays-Bas)",
            information="Né le 31 Juillet 1956",
            creation_date="2024-01-26",
            updating_date="2024-01-26",
            employee_id="9",
        ),
    ]


@pytest.fixture
def fake_contracts_fixture():
    return [
        Contract(
            id="1",
            name="Orange end of year party",
            total_amount="5000",
            pending_amount="2500",
            creation_date="2024-01-26",
            status="1",
            employee_id="1",
        ),
        Contract(
            id="4",
            name="Ubuntu end of year party",
            total_amount="5000",
            pending_amount="2500",
            creation_date="2024-01-26",
            status="1",
            employee_id="4",
        ),
        Contract(
            id="7",
            name="Python end of year party",
            total_amount="5000",
            pending_amount="2500",
            creation_date="2024-01-26",
            status="1",
            employee_id="7",
        ),
    ]


@pytest.fixture
def fake_events_fixture():
    return [
        Event(
            id="",
            name="",
            start_date="",
            end_date="",
            address="",
            attendees="",
            notes="",
            client_id="",
            contract_id="",
        ),
        Event(
            id="",
            name="",
            start_date="",
            end_date="",
            address="",
            attendees="",
            notes="",
            client_id="",
            contract_id="",
        ),
        Event(
            id="",
            name="",
            start_date="",
            end_date="",
            address="",
            attendees="",
            notes="",
            client_id="",
            contract_id="",
        ),
    ]


@pytest.fixture
def employees_fixture(monkeypatch, fake_employees_fixture):
    monkeypatch.setattr(
        "epicevents.models.employee.Employee",
        lambda: fake_employees_fixture,
    )
    return {"employees": fake_employees_fixture}


@pytest.fixture
def clients_fixture(monkeypatch, fake_clients_fixture):
    monkeypatch.setattr(
        "epicevents.models.client.Client",
        lambda: fake_clients_fixture,
    )
    return {"clients": fake_clients_fixture}


@pytest.fixture
def contracts_fixture(monkeypatch, fake_contracts_fixture):
    monkeypatch.setattr(
        "epicevents.models.contract.Contract",
        lambda: fake_contracts_fixture,
    )
    return {"contracts": fake_contracts_fixture}


@pytest.fixture
def events_fixture(monkeypatch, fake_events_fixture):
    monkeypatch.setattr(
        "epicevents.models.event.Event",
        lambda: fake_events_fixture,
    )
    return {"events": fake_events_fixture}
