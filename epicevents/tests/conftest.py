import pytest


fake_employees = [
    {
        "id": "1",
        "username": "Laurent",
        "lastname": "Jouron",
        "email": "laurent@jouron.com",
        "phone": "22 33 44 55 66",
        "password": "$pbkdf2-sha256$29000$6P0/p/QeY.ydMwbAGCOEkHKOsZZSCoEwJkRICWHsndN6r1WqlRKC8L435nxPSUnpXSslZKwV4pxzTknJmZNSKg$i4F8h7.mqBhPQcMM7l.Ge.g8C8UdlRnvg0HK9wNTub0",
        "department_id": "2",
    },
    {
        "id": "2",
        "username": "Antoine",
        "lastname": "Jouron",
        "email": "antoine@jouron.com",
        "phone": "55 66 33 22 55",
        "password": "$pbkdf2-sha256$29000$U0qpFUKIUUoJIaT0/n8PgfD.P2dM6Z0T4nyvNeZ8T8k5hzAGYMwZw5jznjPmfE.pdQ4hZMz5/39vjXEu5Rzj3A$GMRmWOitnqZYchM9e1QncujAozEUewR5p/aix23g6M8",
        "department_id": "3",
    },
    {
        "id": "3",
        "username": "Louis",
        "lastname": "Jouron",
        "email": "louis@jouron.com",
        "phone": "55 11 33 77 99",
        "password": "$pbkdf2-sha256$29000$R4iRMkaoNQaAEAKAUErpvTfm/N8b47w3RihFSGmN0fp/z3nvHUNozblX6l1LiXFubQ1ByPk/J.Scs1YqhXAOgQ$xBXGbXP/R7H9Le4ULM0sAFhon3zVtbiYQQLt.tFZKFA",
        "department_id": "1",
    },
]

fake_clients = [
    {
        "id": "1",
        "compagny_name": "Orange",
        "username": "Stephane",
        "lastname": "Richard",
        "email": "stephane@orange.com",
        "phone": "55 00 33 88 22",
        "address": "Caudréan (France)",
        "information": "Né le 24 Août 1961",
        "creation_date": "2024-01-26",
        "updating_date": "2024-01-26",
        "employee_id": "3",
    },
    {
        "id": "4",
        "compagny_name": "Ubuntu",
        "username": "Mark",
        "lastname": "Shuttleworth",
        "email": "mark@ubuntu.com",
        "phone": "55 77 33 00 11",
        "address": "Welkom (Afrique du sud)",
        "information": "Né le 18 Septembre 1973",
        "creation_date": "2024-01-26",
        "updating_date": "2024-01-26",
        "employee_id": "6",
    },
    {
        "id": "7",
        "compagny_name": "Python",
        "username": "Guido",
        "lastname": "Van rossum",
        "email": "guido@python.com",
        "phone": "33 77 11 00 44",
        "address": "Harlem (Pays-Bas)",
        "information": "Né le 31 Juillet 1956",
        "creation_date": "2024-01-26",
        "updating_date": "2024-01-26",
        "employee_id": "9",
    },
]

fake_contracts = [
    {
        "id": "1",
        "name": "Orange end of year party",
        "total_amount": "5000",
        "pending_amount": "2500",
        "creation_date": "2024-01-26",
        "status": "1",
        "employee_id": "1",
    },
    {
        "id": "4",
        "name": "Ubuntu end of year party",
        "total_amount": "5000",
        "pending_amount": "2500",
        "creation_date": "2024-01-26",
        "status": "1",
        "employee_id": "4",
    },
    {
        "id": "7",
        "name": "Python end of year party",
        "total_amount": "5000",
        "pending_amount": "2500",
        "creation_date": "2024-01-26",
        "status": "1",
        "employee_id": "7",
    },
]

fake_events = [
    {
        "id": "",
        "name": "",
        "start_date": "",
        "end_date": "",
        "address": "",
        "attentes": "",
        "notes": "",
        "client_id": "",
        "contract_id": "",
    },
    {
        "id": "",
        "name": "",
        "start_date": "",
        "end_date": "",
        "address": "",
        "attentes": "",
        "notes": "",
        "client_id": "",
        "contract_id": "",
    },
    {
        "id": "",
        "name": "",
        "start_date": "",
        "end_date": "",
        "address": "",
        "attentes": "",
        "notes": "",
        "client_id": "",
        "contract_id": "",
    },
]


@pytest.fixture
def employees(monkeypatch):
    monkeypatch.setattr("employee", fake_employees)
    return {"employees": fake_employees}


@pytest.fixture
def clients(monkeypatch):
    monkeypatch.setattr("client", fake_clients)
    return {"clients": fake_clients}


@pytest.fixture
def contract(monkeypatch):
    monkeypatch.setattr("contract", fake_contracts)
    return {"contracts": fake_contracts}


@pytest.fixture
def events(monkeypatch):
    monkeypatch.setattr("event", fake_events)
    return {"events": fake_events}
