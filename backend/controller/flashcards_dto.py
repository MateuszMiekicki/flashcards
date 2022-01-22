from multiprocessing.connection import answer_challenge
from unicodedata import category
from pydantic import BaseModel, Required
from typing import List


class Category(BaseModel):
    name: str


class Subcategory(BaseModel):
    name: str
    category_name: str


class Question(BaseModel):
    content: str


class QuestionAnswer(BaseModel):
    content: str
    is_correct_answer: bool


class Card(BaseModel):
    question: Question
    answer: QuestionAnswer


class SetCard(BaseModel):
    name: str
    category_name: str
    subcategory_name: str
    cards: List[Card] = list()
