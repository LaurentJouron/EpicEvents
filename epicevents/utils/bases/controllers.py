class BaseController:
    """
    Base controller class.

    Explanation:
    This class serves as the base for all controllers in the application. It
    provides a common structure and methods that can be inherited by specific
    controllers.

    Methods:
    - action(): Raises a NotImplementedError. Subclasses should override this
    method to define their specific action.
    - run(): Executes the action method of the controller and returns the
    result.

    """

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def action(self):
        """
        Raises a NotImplementedError.

        Explanation:
        This method should be overridden by subclasses to define the specific
        action of the controller.

        """
        raise NotImplementedError

    def run(self):
        """
        Executes the action method of the controller and returns the result.

        Returns:
        The result of the action method.

        """
        return self.action()
