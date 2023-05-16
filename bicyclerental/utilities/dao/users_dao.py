from typing import Any, List, Union
from sqlalchemy.orm.session import Session
from bicyclerental.models.users_model import Users
from bicyclerental.utilities.dao.abstract_dao import DAO
from sqlalchemy.orm.query import Query 

class UsersDao(DAO):
    
    def __init__(self, session: Session) -> None:
        """
        Args:
            session (Session): session object that use to connect with database.
        """
        self.__model = Users
        super().__init__(session, self.__model)
        
    def get_user_from_id(self, id: int) -> Union[List[Any], None]:
        """This function return list of user by getting user id.

        Args:
            id (int): id of user.

        Returns:
            Union[List[Any], None]: List of Users.
        """
        result = self._query(self.__model.id == id)
        return result
    
    def get_user_from_name(self, firstname: str) -> Union[List[Any], None]:
        """This function return list of user by getting firstname.

        Args:
            firstname (str): firstname of user.

        Returns:
            Union[List[Any], None]: List of Users.
        """
        result = self._query(self.__model.firstname == firstname)
        return result
    
    def get_user_from_lastname(self, lastname: str) -> Union[List[Any], None]:
        """This function return list of user by getting lastname.

        Args:
            lastname (str): lastname of user.

        Returns:
            Union[List[Any], None]: List of Users.
        """
        result = self._query(self.__model.lastname == lastname)
        return result
        
    def get_user_from_age(self, age: int) -> Union[List[Any], None]:
        """This function return list of user by getting user age.

        Args:
            age (int): age of user.

        Returns:
            Union[List[Any], None]: List of Users.
        """
        result = self._query(self.__model.age == age)
        return result