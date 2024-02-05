# from epicevents.utils.contants import SHORT_SLEEP
# import pytest
# from typer.testing import CliRunner
# from epicevents.utils.bases.views import BaseSuccessView

# runner = CliRunner()


# # BaseSuccessView tests
# @pytest.mark.parametrize(
#     "message, test_id",
#     [
#         ("Creating successfully", "TC1"),
#         ("Updated successfully", "TC2"),
#         ("Deleted successfully", "TC3"),
#     ],
# )
# def test_success_message(message, test_id, mock_console, mock_time_sleep):
#     # Arrange
#     view = BaseSuccessView()
#     view.console = mock_console

#     # Act
#     view._success_message(message)

#     # Assert
#     mock_console.rule.assert_called_with("[bold green]SUCCESS")
#     mock_console.print.assert_called_with(
#         f"\n✔️ {message}", style="bold green", justify="center"
#     )
#     mock_time_sleep.assert_called_with(SHORT_SLEEP)
#     assert mock_console.clear.call_count == 2
