import typer

from .database import Model, engine
from .views.home_views import ExitView
from .controllers import HomeController

exit_view = ExitView()


def main():
    Model.metadata.create_all(engine)
    controller = HomeController()
    while controller is not None:
        next_controller = controller.run()
        controller = next_controller
    exit_view.good_by()


if __name__ == "__main__":
    typer.run(main)
