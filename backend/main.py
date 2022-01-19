from fastapi import FastAPI
from backend.controller import user
from backend.configure import database
from fastapi.security import HTTPBearer
from backend.security.authenticate import Authenticate
app = FastAPI()
app.include_router(user.router)


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


@app.get("/")
def hello_world():
    return {"Hello": "World"}
