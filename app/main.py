from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.entity.user import User, Role, User_type
from app.repository.user_repository import User_repository
import bcrypt


def insert_example(session):
    new_user = User(login='new_user', email='new_user@test.com',
                    password='super trudne haslo!@#', role_id=3, user_type_id=2)
    user_repository = User_repository(session)
    new_user_id = user_repository.insert(new_user)

    if new_user_id is None:
        print('nope')
    else:
        print(new_user_id)


def login_example(session):
    example_password = 'wrong_password'
    example_login = 'new_user_but_not_exists'

    user_repository = User_repository(session)
    if user_repository.getByLogin(example_login):
        print('exists')
    else:
        print('user not exists')

    example_password = 'super trudne haslo!@#'
    example_login = 'new_user'
    user_from_db = user_repository.getByLogin(example_login)
    if user_from_db:
        if bcrypt.checkpw(example_password.encode("utf-8"),
                          user_from_db.password.encode("utf-8")):
            print("ok")


if __name__ == "__main__":
    engine = create_engine('postgresql://byt:byt!123@localhost:5400/byt')
    session = Session(engine)

    insert_example(session)
    login_example(session)
    