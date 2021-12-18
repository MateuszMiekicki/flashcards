from fastapi import FastAPI
from backend.controller import login, register
from backend.database import db
app = FastAPI()
app.include_router(login.router)
app.include_router(register.router)


@app.on_event("startup")
async def startup():
    auth = db.DatabaseAuth("byt", "byt!123")
    address = db.DatabaseAddress("localhost", 5400)
    dialect = db.Dialect.postgresql
    driver = db.Driver.none
    database = "byt"
    app.state.db = db.Database().connect(dialect, driver, address, database, auth)


@app.get("/")
def read_root():
    return {"Hello": "World"}

# if __name__ == "__main__":
#     from backend.entity.entity import Role_entity, User_entity
#     from sqlalchemy.orm import Session
#     from sqlalchemy import create_engine

#     engine = create_engine('postgresql://byt:byt!123@localhost:5400/byt')
#     session = Session(engine)
#     login = 'admin'
#     print(session.query(User_entity).filter(User_entity.login == login).first())
