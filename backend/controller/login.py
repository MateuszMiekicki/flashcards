from fastapi.security import OAuth2PasswordRequestForm
from fastapi import status, HTTPException, APIRouter, Request
from backend.controller.dto.user import Login
from backend.repository.user import User_repository
import bcrypt
router = APIRouter()


@router.post("/login", status_code=status.HTTP_201_CREATED)
async def login(request: Request, user: Login):
    user_repo = User_repository(request.app.state.db)
    if user_repo.authenticate(user.login, user.password) is not True:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
    return {
        "access_token": " create_access_token(sub=user.id)",
        "token_type": "bearer",
    }
