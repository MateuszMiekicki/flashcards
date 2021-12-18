from pydantic import BaseModel, Required
from typing import Optional


class Register(BaseModel):
    login: str
    email: str
    password: str


class Login(BaseModel):
    login: Optional[str]
    email: Optional[str]
    password: str
