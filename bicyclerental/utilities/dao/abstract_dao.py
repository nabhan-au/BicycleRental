from typing import Any, Union, List
from sqlalchemy.orm.session import Session
from bicyclerental.models.bicycle_model import Bicycle
from bicyclerental.models.users_model import Users

class DAO():
    
    def __init__(self, session: Session, model: Union[Bicycle, Users]) -> None:
        """
        Args:
            session (Session): session object that use to connect with database.
            model (Union[Bicycle, Users]): Model of database schema.
        """
        self.__session = session
        self.__model = model
        
    def _query(self,*filter: Any) -> Union[List[Any], None]:
        """This function get expression and return the result of query.

        Returns:
            Union[List[Any], None]: Return list of result.
        """
        try:
            result = self.__session.query(self.__model).filter(*filter).all()
            return result
        except Exception as e:
            print(e)
            