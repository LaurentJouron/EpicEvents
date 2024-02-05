from epicevents.utils.contants import SHORT_SLEEP
import pytest
from typer.testing import CliRunner
from epicevents.utils.bases.views import BaseView

runner = CliRunner()


# BaseView tests
@pytest.mark.parametrize(
    "title, stars, test_id",
    [
        ("Centered Title", True, "TC1"),
        ("Another Title", False, "TC2"),
    ],
)
def test_display_centered_title(
    title, stars, test_id, mock_console, mock_time_sleep
):
    # Arrange
    view = BaseView()

    # Act
    view._display_centered_title(title, stars)

    # Assert
    title_str = f"\n ✨{title}✨ " if stars else title
    mock_console.print.assert_called_with(
        title_str, style="bold blue", justify="center"
    )
    mock_time_sleep.assert_called_with(SHORT_SLEEP)
    mock_console.clear.assert_called_once()
