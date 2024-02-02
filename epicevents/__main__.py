from .database import Model, engine
from .views.home_views import ExitView
from .controllers import ReceptionController
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
import typer


exit_view = ExitView()


def main():
    """
    Runs the main function of the application.

    Creates the database tables using the Model metadata and engine.
    Initializes the ReceptionController and enters a loop to execute the
    controller's run method.
    Displays a goodbye message when the loop is exited.

    Args:
        None

    Returns:
        None

    Examples:
        >>> main()
        Database tables created.
        Welcome to EpicEvents!
        ...
        Goodbye! Thank you for using EpicEvents.
    """
    # import sentry_sdk

    sentry_sdk.init(
        dsn="https://44c71e14b86c0aafc7e4d7d2cdf4e7d6@us.sentry.io/4506677090189312",
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
    )
    Model.metadata.create_all(engine)
    controller = ReceptionController()
    while controller is not None:
        next_controller = controller.run()
        controller = next_controller
    exit_view.good_by()


if __name__ == "__main__":
    typer.run(main)
