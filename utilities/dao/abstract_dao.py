from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base

from models.users_model import Users
Base = declarative_base()

class DAO():
    
    def __init__(self, session: Session, model: Base) -> None:
        self.__session = session
        self.__model = model
        
    def _query(self,*filter):
        try:
            result = self.__session.query(self.__model).filter(*filter).all()
            return result
        except Exception as e:
            print(e)
            