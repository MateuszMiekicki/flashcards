from fastapi import FastAPI
from backend.controller import login
app = FastAPI()
app.include_router(login.router)

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
    