from fastapi import APIRouter
from fastapi import status, HTTPException
from backend.controller.dto.user import Login
router = APIRouter()


@router.post("/login", status_code=status.HTTP_201_CREATED)
async def login(user: Login):
    # if user_repo.is_user_exist(user.login, user.email):
    # raise HTTPException(status_code=status.HTTP_409_CONFLICT,
    #                     detail=f'User {user.email}/{user.login} exists')
    # user_entity = User_entity(user.email, user.login, user.password)
    # user_repo.insert(user_entity)
    raise HTTPException(status_code=status.HTTP_200_OK,
                        detail=f'TEST')
