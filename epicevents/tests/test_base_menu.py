# import pytest
# from typer.testing import CliRunner
# from epicevents.utils.bases.views import BaseMenu

# runner = CliRunner()


# # BaseMenu tests
# @pytest.mark.parametrize(
#     "menu_name, menu, choice, expected, test_id",
#     [
#         ("Main Menu", {"1": "Option 1", "2": "Option 2"}, "1", "1", "TC1"),
#         ("Main Menu", {"1": "Option 1", "2": "Option 2"}, "3", "3", "TC2"),
#         # Add more test cases for each menu method
#     ],
# )
# def test_choice_menu(
#     menu_name, menu, choice, expected, test_id, mock_console, mock_typer_prompt
# ):
#     # Arrange
#     menu_view = BaseMenu()
#     menu_view.console = mock_console
#     mock_typer_prompt.return_value = choice

#     # Act
#     result = menu_view._choice_menu(menu_name, menu)

#     # Assert
#     assert result == expected
