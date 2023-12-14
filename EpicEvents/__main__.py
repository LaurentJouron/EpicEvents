from .controllers import AuthenticationController
from .views import ExitView

exit_view = ExitView()


def run_application():
    controller = AuthenticationController()
    while controller is not None:
        next_controller = controller.run()
        controller = next_controller
    exit_view.good_by()


run_application()
