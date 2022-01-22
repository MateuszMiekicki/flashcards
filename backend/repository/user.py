import backend.entity.user as entity
from sqlalchemy.orm import Session


class User():
    def __init__(self, session: Session):
        self.session = session

    def is_exist_login(self, user_login: str):
        return self.session.query(entity.User.id).filter_by(login=user_login).first() is not None

    def is_exist_email(self, user_email: str):
        return self.session.query(entity.User.id).filter_by(email=user_email).first() is not None

    def is_user_exist(self, user_login: str, user_email: str):
        return self.is_exist_login(user_login) == True and self.is_exist_email(user_email) == True

    def insert(self, user_entity: entity.User):
        self.session.add(user_entity)
        self.session.commit()