from backend.repository.user import User_repository
from fastapi import APIRouter
from fastapi import status, HTTPException
from backend.entity.entity import User_entity
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine('postgresql://byt:byt!123@localhost:5400/byt')
session = Session(engine)
user_repo = User_repository(session)
router = APIRouter()


class User(BaseModel):
    login: str
    email: str
    password: str
    

@router.post("/login", status_code=status.HTTP_201_CREATED)
async def login(user: User):
    if user_repo.is_user_exist(user.login, user.email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'User {user.email}/{user.login} exists')
    user_entity = User_entity(user.email, user.login, user.password)
    user_repo.insert(user_entity)
