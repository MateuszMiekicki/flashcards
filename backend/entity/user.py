from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    login = Column(String, nullable=False, unique=True)
    is_activate = Column(Boolean, nullable=False)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
    role = relationship('Role', backref='user')
    user_type_id = Column(Integer, ForeignKey('user_type.id'), nullable=False)
    user_type = relationship('User_type', backref='user')

    def __init__(self, email: str, login: str, password: str):
        self.email = email
        self.login = login
        self.password = password
        self.user_type_id = 1
        self.role_id = 3
        self.is_activate = True


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    role = Column(String, nullable=False, unique=True)


class User_type(Base):
    __tablename__ = 'user_type'

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False, unique=True)
