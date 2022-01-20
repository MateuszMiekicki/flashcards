from sqlalchemy.sql import select
import backend.entity.flashcards as entity
from sqlalchemy.orm import Session
import json


class Category():
    def __init__(self, session: Session):
        self.session = session

    def insert(self, category_entity: entity.Category):
        self.session.add(category_entity)
        self.session.commit()

    def select_all(self):
        categories = []
        for c in self.session.query(entity.Category).all():
            categories.append({'id': c.id, 'name': c.name})
        return categories

    def category_id(self, category_name: str):
        return self.session.query(entity.Category.id).filter_by(name=category_name).first()


class Subcategory():
    def __init__(self, session: Session):
        self.session = session

    def insert(self, subcategory_entity: entity.Subcategory):
        self.session.add(subcategory_entity)
        self.session.commit()

    def select_all_subcategories_from_category(self, category_name: str):
        categories = []
        for c in self.session.query(entity.Subcategory).filter_by(category_id=(
            select(entity.Category.id)
            .where(entity.Category.name == category_name)
        ).as_scalar()):
            categories.append({'id': c.id, 'name': c.name})
        return categories

    def subcategory_id(self, category_id_: int, subcategory_name: str):
        return self.session.query(entity.Subcategory.id).filter_by(category_id=category_id_,
                                                                   name=subcategory_name).first()
