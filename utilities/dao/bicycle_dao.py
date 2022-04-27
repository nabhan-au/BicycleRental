from typing import Any, List, Union
from sqlalchemy.orm.session import Session
from models.bicycle_model import Bicycle
from utilities.dao.abstract_dao import DAO
from sqlalchemy.orm.query import Query

class BicycleDAO(DAO):
    
    def __init__(self, session: Session) -> None:
        """
        Args:
            session (Session): session object that use to connect with database.
        """
        self.__model = Bicycle
        super().__init__(session, self.__model)
        
    def get_bicycle_from_id(self, id: int) -> Union[List[Any], None]:
        """This function return List of Bicycle by getting id.

        Args:
            id (int): id of bicycle.

        Returns:
            Union[List[Any], None]: List of Bicycle object.
        """
        result = self._query(self.__model.id == id)
        return result
    
    def get_bicycle_from_brand(self, brand: str) -> Union[List[Any], None]:
        """This function return return List of Bicycle by getting brand.

        Args:
            brand (str): brand of bicycle.

        Returns:
            Union[List[Any], None]: List of Bicycle object.
        """
        result = self._query(self.__model.brand == brand)
        return result
    
    def get_bicycle_from_type(self, type: str) -> Union[List[Any], None]:
        """This function return return List of Bicycle by getting type.
        Args:
            type (str): type of bicycle.

        Returns:
            Union[List[Any], None]: List of Bicycle object.
        """
        result = self._query(self.__model.type == type)
        return result