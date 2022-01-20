from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

    def __init__(self, name: str):
        self.name = name


class Subcategory(Base):
    __tablename__ = 'subcategory'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    category = relationship('Category', backref='subcategory')

    def __init__(self, name: str, category_id: int):
        self.name = name
        self.category_id = category_id
