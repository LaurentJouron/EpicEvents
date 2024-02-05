# import pytest
# from typer.testing import CliRunner
# from epicevents.utils.bases.views import BaseManageConsole

# runner = CliRunner()


# # BaseManageConsole tests
# @pytest.mark.parametrize("test_id", ["TC1", "TC2"])
# def test_clean_console(test_id, mock_console):
#     # Arrange
#     console = BaseManageConsole()
#     console.console = mock_console

#     # Act
#     console._clean_console()

#     # Assert
#     mock_console.clear.assert_called_once()


# @pytest.mark.parametrize(
#     "title, test_id",
#     [
#         ("Test Title", "TC1"),
#         ("Another Title", "TC2"),
#     ],
# )
# def test_display_title(title, test_id, mock_console):
#     # Arrange
#     console = BaseManageConsole()
#     console.console = mock_console

#     # Act
#     console._display_title(title)

#     # Assert
#     mock_console.rule.assert_called_once_with(f"[bold blue]{title}")
