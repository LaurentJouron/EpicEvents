def test_example(
    employees_fixture, clients_fixture, contracts_fixture, events_fixture
):
    employees_data = employees_fixture["employees"]
    clients_data = clients_fixture["clients"]
    contracts_data = contracts_fixture["contracts"]
    events_data = events_fixture["events"]

    assert len(employees_data) == 3
    assert len(clients_data) == 3
    assert len(contracts_data) == 3
    assert len(events_data) == 3
