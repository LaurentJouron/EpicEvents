# import pytest
# from typer.testing import CliRunner
# from epicevents.utils.bases.views import BaseAnswerView

# runner = CliRunner()


# # BaseAnswerView tests
# @pytest.mark.parametrize(
#     "prompt, input_value, expected, test_id",
#     [
#         ("username", "john", "John", "TC1"),
#         ("lastname", "doe", "Doe", "TC2"),
#         # Add more test cases for each input method
#     ],
# )
# def test_get_answer(
#     prompt, input_value, expected, test_id, mock_console, mock_typer_prompt
# ):
#     # Arrange
#     view = BaseAnswerView()
#     view.console = mock_console
#     mock_typer_prompt.return_value = input_value

#     # Act
#     result = (
#         view._get_username() if prompt == "username" else view._get_lastname()
#     )

#     # Assert
#     mock_typer_prompt.assert_called_with(f"\nPlease enter the {prompt} ")
#     assert result == expected
