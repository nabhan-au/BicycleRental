from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utilities.dao.bicycle_dao import BicycleDAO

from utilities.dao.users_dao import UsersDao

class SessionDB:

    def __init__(self) -> None:
        self.__engine = create_engine('sqlite:///rental.db', echo=True)
        session = sessionmaker(bind=self.__engine)
        self.__session = session()

    def get_users(self) -> UsersDao:
        return UsersDao(self.__session)

    def get_bicycle(self) -> BicycleDAO:
        return BicycleDAO(self.__session)
