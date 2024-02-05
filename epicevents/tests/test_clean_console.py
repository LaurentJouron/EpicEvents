import pytest
from unittest.mock import patch
from typer.testing import CliRunner

runner = CliRunner()


@pytest.fixture
def mock_console():
    with patch("epicevents.utils.bases.views.Console") as mock:
        yield mock


@pytest.fixture
def mock_typer_prompt():
    with patch("typer.prompt") as mock:
        yield mock


@pytest.fixture
def mock_typer_confirm():
    with patch("typer.confirm") as mock:
        yield mock


@pytest.fixture
def mock_time_sleep():
    with patch("time.sleep", return_value=None) as mock:
        yield mock
