from .database import Model, engine
from .utils.contants import SENTRY_DSN
from .views.home_views import ExitView
from .controllers import ReceptionController
import sentry_sdk
import logging
from sentry_sdk.integrations.logging import LoggingIntegration
import typer


exit_view = ExitView()
logging.basicConfig(level=logging.INFO)


def main():
    """
    Runs the main function of the application.

    Creates the database tables using the Model metadata and engine.
    Initializes the ReceptionController and enters a loop to execute the
    controller's run method.
    Displays a goodbye message when the loop is exited.

    Examples:
        >>> main()
        Database tables created.
        Welcome to EpicEvents!
        ...
        Goodbye! Thank you for using EpicEvents.
    """
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
        enable_tracing=True,
        debug=False,
        environment="development",
        integrations=[
            LoggingIntegration(level=logging.INFO, event_level=logging.INFO),
        ],
    )
    Model.metadata.create_all(engine)
    controller = ReceptionController()
    while controller is not None:
        next_controller = controller.run()
        controller = next_controller
    exit_view.good_by()


if __name__ == "__main__":
    typer.run(main)
