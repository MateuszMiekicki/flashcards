from sqlalchemy.orm import Session
from app.entity.user import User
from sqlalchemy.sql import exists
from sqlalchemy import or_, literal, exc
import bcrypt


class User_repository:
    def __init__(self, dbSession):
        self.session = dbSession

    def insert(self, entity: User):
        if not self.isUnique(entity.email, entity.login):
            return None
        entity.password = str(bcrypt.hashpw(
            entity.password.encode('utf-8'), bcrypt.gensalt(10)), 'utf-8')
        try:
            self.session.add(entity)
            self.session.commit()
            return entity.id
        except exc.IntegrityError:
            return None

    def update(self, userId: int, newEntity: User):
        pass

    def isExistLogin(self, login: str):
        return self.session.query(
            exists().where(User.login == login)).scalar()

    def isExistEmail(self, email: str):
        return self.session.query(
            exists().where(User.email == email)).scalar()

    def isUnique(self, email: str, login: str):
        return self.session.query(User).filter(User.email == email,
                                               User.login == login).count() == 0

    def getByLogin(self, login: str):
        return self.session.query(User).filter(User.login == login).first()

    def getByEmail(self, email: str):
        return self.session.query(User).filter(User.email == email).first()
