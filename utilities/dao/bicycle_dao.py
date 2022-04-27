import re
from unittest import result
from sqlalchemy.orm.session import Session
from models.bicycle_model import Bicycle
from utilities.dao.abstract_dao import DAO

class BicycleDAO(DAO):
    
    def __init__(self, session: Session) -> None:
        self.__model = Bicycle
        super().__init__(session, self.__model)
        
    def get_bicycle_from_id(self, id):
        result = self._query(Bicycle.id == id)
        return result
    
    def get_bicycle_from_brand(self, brand):
        result = self._query(Bicycle.brand.contains(brand))
        return result
    
    def get_bicycle_from_type(self, type):
        result = self._query(Bicycle.type == type)
        return result