from utils.bases.menus import BaseMenu
from utils.bases.views import BaseView


class RoleView(BaseView):
    def add_role(self):
        self._get_string("Enter a new role: ")
