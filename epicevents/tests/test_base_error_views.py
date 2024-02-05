# from epicevents.utils.contants import SHORT_SLEEP
# import pytest
# from typer.testing import CliRunner
# from epicevents.utils.bases.views import BaseErrorView

# runner = CliRunner()


# # BaseErrorView tests
# @pytest.mark.parametrize(
#     "method, message, test_id",
#     [
#         ("_not_found", " Not found.", "TC1"),
#         ("_invalid_id", " Is no valid.", "TC2"),
#         ("_exist_error", " Is already registered.", "TC3"),
#         # Add more test cases for each error method
#     ],
# )
# def test_error_messages(
#     method, message, test_id, mock_console, mock_time_sleep
# ):
#     # Arrange
#     view = BaseErrorView()
#     view.console = mock_console

#     # Act
#     getattr(view, method)()

#     # Assert
#     mock_console.rule.assert_called_with("[bold red]ERROR")
#     mock_console.print.assert_called_with(
#         f"\n⛔️ {message}", style="bold red", justify="center"
#     )
#     mock_time_sleep.assert_called_with(SHORT_SLEEP)
#     assert mock_console.clear.call_count == 2
