from pydantic import BaseModel, Required
from typing import Optional


class Category(BaseModel):
    name: str


class Subcategory(BaseModel):
    name: str
    category_name: str
