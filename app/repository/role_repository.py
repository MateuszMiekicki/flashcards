from app.entity.user import Role, User


class Role_repository:
    def __init__(self, dbSession):
        self.session = dbSession

    def get_all_roles(self):
        return self.session.query(Role).all()

    def get_all_user_by_role(self, role: Role):
        return self.session.query(User).filter(User.role_id == role.id).all()
