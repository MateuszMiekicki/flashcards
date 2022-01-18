from fastapi.security import OAuth2PasswordRequestForm
from fastapi import status, HTTPException, APIRouter, Request
from backend.controller.dto.user import Login
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import FastAPI, HTTPException, Security
import bcrypt
router = APIRouter()
security = HTTPBearer()


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(request: Request, user: Login):
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
    print(request.app.state.authenticate.decode_token(token))
    if(request.app.state.authenticate.decode_token(token)):
        return 'Top Secret data only authorized users can access this info'


@router.get('/notsecret')
def not_secret_data():
    return 'Not secret data'
