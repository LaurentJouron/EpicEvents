import typer

from .views import ExitView
from .controllers import ReceptionController
from .database import Model, engine
from .models import Role, Employee, Client, Event, Contract

exit_view = ExitView()


def run_application():
    controller = ReceptionController()
    while controller is not None:
        next_controller = controller.run()
        controller = next_controller
    exit_view.good_by()


def main():
    Model.metadata.create_all(engine)
    Role()
    Employee()
    Client()
    Event()
    Contract()


if __name__ == "__main__":
    typer.run(main)

run_application()
