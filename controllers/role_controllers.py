from sqlalchemy import select
from EpicEvents.database import Session
from utils.bases.controllers import BaseController
from models.role import Role
from views.role_views import RoleView

view = RoleView()


class AddRoleController(BaseController):
    def run(self):
        with Session() as session:
            with session.begin():
                role = view.add_role()
                new_role = Role(name=role)
                session.add(new_role)


class GetRoleController(BaseController):
    def run(self):
        with Session() as session:
            with session.begin():
                query = select(Role).join().where()
                for role in session.scalars(query):
                    print(f"- {role}")
