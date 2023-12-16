import typer

from .views.home_views import ExitView
from .models import Role, Employee, Client, Event, Contract
from .controllers import ReceptionController
from .database import Model, engine

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
