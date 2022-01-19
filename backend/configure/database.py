from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from typing import Optional
from enum import Enum


class Dialect(Enum):
    postgresql = "postgresql"


class Driver(Enum):
    none = ''


class DatabaseAuth:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def get_auth(self):
        return f"{self.username}:{self.password}"


class DatabaseAddress:
    def __init__(self, address: str, port: int):
        self.address = address
        self.port = port

    def get_address(self):
        return f"{self.address}:{self.port}"


class Database:
    def __create_address(self, dialect: Dialect, driver: Driver,
                         address: DatabaseAddress, database: str,
                         auth: DatabaseAuth):
        if driver != Driver.none:
            driver = f'+{driver.value}'
        else:
            driver = ''
        return f"{dialect.value}{driver}://{auth.get_auth()}@{address.get_address()}/{database}"

    def connect(self, dialect: Dialect, driver: Driver,
                address: DatabaseAddress, database: str,
                auth: DatabaseAuth):
        url = self.__create_address(dialect, driver, address, database, auth)
        self.engine = create_engine(url)
        self.session = Session(self.engine)
        return self.session