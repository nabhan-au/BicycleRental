from sqlalchemy.orm.session import Session
from models.users_model import Users
from utilities.dao.abstract_dao import DAO 

class UsersDao(DAO):
    
    def __init__(self, session: Session) -> None:
        self.__model = Users
        super().__init__(session, self.__model)
        
    def get_user_from_id(self, id):
        result = self._query(self.__model.id == id)
        return result
    
    def get_user_from_name(self, firstname):
        result = self._query(self.__model.firstname == firstname)
        return result
    
    def get_user_from_lastname(self, lastname):
        result = self._query(self.__model.lastname == lastname)
        return result
        
    def get_user_from_age(self, age):
        result = self._query(self.__model.age == age)
        return result