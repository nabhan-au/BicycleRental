from curses import echo
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from utilities.dao.users_dao import UsersDao

class RentalDB:
    
    def __init__(self) -> None:
        self.__engine = create_engine('sqlite://rental.db:', echo=True)
        session = sessionmaker(bind=self.__engine)
        self.__session = session.begin()
        
    def get_users(self):
        return UsersDao(self.__session)