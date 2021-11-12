from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
    user_type_id = Column(Integer, ForeignKey('user_type.id'), nullable=False)


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    role = Column(String, nullable=False, unique=True)
    user = relationship("User")


class User_type(Base):
    __tablename__ = 'user_type'

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False, unique=True)
    user = relationship("User")
