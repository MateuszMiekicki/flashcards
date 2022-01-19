from fastapi import APIRouter, status, Request, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import backend.controller.user_dto as dto
import backend.repository.user as repository
import backend.entity.user as entity
import bcrypt
router = APIRouter()
security = HTTPBearer()


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


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(request: Request, user: dto.Login):
    user_from_db = request.app.state.authenticate.authenticate(
        user.login, user.password)
    if user_from_db is None:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
    access_token = request.app.state.authenticate.encode_token(user_from_db)
    refresh_token = request.app.state.authenticate.encode_refresh_token(
        user_from_db)
    return {'access_token': access_token, 'refresh_token': refresh_token}


@router.get('/refresh_token')
def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    refresh_token = credentials.credentials
    new_token = auth_handler.refresh_token(refresh_token)
    return {'access_token': new_token}


@router.post('/secret')
def secret_data(request: Request, credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    if(request.app.state.authenticate.decode_token(token)):
        return 'Top Secret data only authorized users can access this info'
