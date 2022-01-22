from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship
from backend.entity.user import User
from backend.entity.base import Base


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


class SetCards(Base):
    __tablename__ = 'set_cards'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    subcategory_id = Column(Integer, ForeignKey(
        'subcategory.id'), nullable=False)
    subcategory = relationship('Subcategory', backref='set_cards')
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', backref='set_cards')

    def __init__(self, name: str, subcategory_id: int, user_id: int):
        self.name = name
        self.subcategory_id = subcategory_id
        self.user_id = user_id


class Card(Base):
    __tablename__ = 'card'

    id = Column(Integer, primary_key=True)
    set_cards_id = Column(Integer, ForeignKey(
        'set_cards.id'), nullable=False)
    set_cards = relationship('SetCards', backref='card')

    def __init__(self, set_cards_id: int):
        self.set_cards_id = set_cards_id


class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False, unique=True)
    card_id = Column(Integer, ForeignKey(
        'card.id'), nullable=False)
    card = relationship('Card', backref='question')

    def __init__(self, content: str, card_id: int):
        self.content = content
        self.card_id = card_id


class QuestionAnswer(Base):
    __tablename__ = 'question_answer'

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False, unique=True)
    is_correct_answer = Column(String, nullable=False, unique=True)
    question_id = Column(Integer, ForeignKey(
        'question.id'), nullable=False)
    question = relationship('Question', backref='question')

    def __init__(self, content: str, is_correct_answer: bool, question_id: int):
        self.content = content
        self.is_correct_answer = is_correct_answer
        self.question_id = question_id
