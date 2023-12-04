from .controllers import HomeController
from .views import HomeView

view = HomeView()


def run_application():
    controller = HomeController()
    while controller is not None:
        next_controller = controller.run()
        controller = next_controller
    view.good_by()


run_application()
