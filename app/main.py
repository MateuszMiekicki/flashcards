from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.entity.user import User, Role, User_type
from app.repository.user_repository import User_repository
from app.repository.role_repository import Role_repository
import bcrypt


def insert_example(session):
    new_user = User('new_user@test.com', 'new_user', 'super trudne haslo!@#')
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


# def update_role_example(session):
#     user_repository = User_repository(session)

#     user = user_repository.getByLogin('user@flashcards.com')

#     user_repository.change_role(user, )

def print_all_role(session):
    role_repository = Role_repository(session)
    roles = role_repository.get_all_roles()
    for role in roles:
        print(role.role)


def get_all_user_by_role(session):
    role_repository = Role_repository(session)
    roles = role_repository.get_all_roles()
    for role in roles:
        print(role.role)
        for user in role_repository.get_all_user_by_role(role):
            print(user.id)


def get_user_role(session, user: User):
    user_repository = User_repository(session)
    user = user_repository.get_role(user)
    print(user.email)
    print(user.role.role)


if __name__ == "__main__":
    engine = create_engine('postgresql://byt:byt!123@localhost:5400/byt')
    session = Session(engine)

    insert_example(session)
    login_example(session)
    print_all_role(session)
    get_all_user_by_role(session)

    user_repository = User_repository(session)
    user = user_repository.getByEmail('admin@flashcards.com')
    get_user_role(session, user)
