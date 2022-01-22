from fastapi import FastAPI
from sqlalchemy import false
from backend.controller import user, flashcards
from backend.configure import database
from fastapi.security import HTTPBearer
from backend.security.authenticate import Authenticate
import backend.entity.user as entity
import backend.controller.user_dto as dto
import backend.repository.user as repository
import bcrypt
app = FastAPI()
app.include_router(user.router)
app.include_router(flashcards.router)


@app.on_event("startup")
async def startup():
    auth = database.DatabaseAuth("byt", "byt!123")
    address = database.DatabaseAddress("localhost", 5400)
    dialect = database.Dialect.postgresql
    driver = database.Driver.none
    database_name = "byt"
    app.state.database = database.Database().connect(
        dialect, driver, address, database_name, auth)
    app.state.authenticate = Authenticate(app.state.database)
    app.state.security = HTTPBearer()

    repo = repository.User(app.state.database)
    if repo.is_user_exist("admin", "admin") is False:
        pwhash = bcrypt.hashpw("admin".encode('utf8'), bcrypt.gensalt())
        password = pwhash.decode('utf8')
        user_entity = entity.User("admin", "admin", password, 1)
        repo.insert(user_entity)


@app.get("/")
def hello_world():
    return {"Hello": "World"}
