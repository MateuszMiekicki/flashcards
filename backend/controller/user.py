from fastapi import APIRouter, status, Request, HTTPException
import backend.controller.user_dto as dto
import backend.repository.user as repository
import backend.entity.user as entity
import bcrypt
router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def login(request: Request, user: dto.Register):
    repo = repository.User(request.app.state.database)
    if repo.is_user_exist(user.login, user.email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'User {user.email} or {user.login} exists')
    pwhash = bcrypt.hashpw(user.password.encode('utf8'), bcrypt.gensalt())
    user.password = pwhash.decode('utf8')
    user_entity = entity.User(user.email, user.login, user.password)
    repo.insert(user_entity)
