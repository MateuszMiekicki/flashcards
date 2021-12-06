from backend.entity.entity import Role_entity, User_entity
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine('postgresql://byt:byt!123@localhost:5400/byt')
session = Session(engine)


class User_repository():
    def __init__(self, session: Session):
        self.session = session

    def is_exist_login(self, user_login: str):
        return session.query(User_entity.id).filter_by(login=user_login).first() is not None

    def is_exist_email(self, user_email: str):
        return session.query(User_entity.id).filter_by(email=user_email).first() is not None

    def is_user_exist(self, user_login: str, user_email: str):
        return self.is_exist_login(user_login) == True and self.is_exist_email(user_email) == True

    def insert(self, user_entity: User_entity):
        session.add(user_entity)
        session.commit()