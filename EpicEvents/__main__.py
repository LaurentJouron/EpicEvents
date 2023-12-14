import typer
from .controllers import AuthenticationController
from .views import ExitView
from .database import Model, engine

from models.role import Role

exit_view = ExitView()


def run_application():
    controller = AuthenticationController()
    while controller is not None:
        next_controller = controller.run()
        controller = next_controller
    exit_view.good_by()


def main():
    Model.metadata.create_all(engine)
    Role()


if __name__ == "__main__":
    typer.run(main)

run_application()
