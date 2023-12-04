class BaseController:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def action(self):
        raise NotImplementedError

    def run(self):
        return self.action()
