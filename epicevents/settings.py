from .models import RoleManager

role_manager = RoleManager()


def role_settings():
    roles = ("Commercial", "Gestion", "Support")
    for role in roles:
        role_manager.add_role(role)
