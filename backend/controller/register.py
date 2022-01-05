from fastapi import status, HTTPException
from fastapi import APIRouter, Request
import bcrypt
from backend.controller.dto.user import Register
from backend.database.entity.entity import User_entity
from backend.repository.user import User_repository
router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def login(request: Request, user: Register):
    user_repo = User_repository(request.app.state.db)
    if user_repo.is_user_exist(user.login, user.email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'User {user.email} or {user.login} exists')
    pwhash = bcrypt.hashpw(user.password.encode('utf8'), bcrypt.gensalt())
    user.password = pwhash.decode('utf8')
    user_entity = User_entity(user.email, user.login, user.password)
    user_repo.insert(user_entity)
