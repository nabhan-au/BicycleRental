from sqlalchemy.orm.session import Session
from models.users_model import Users

class UsersDao():
    
    def __init__(self, session: Session) -> None:
        self.__session = session
        self.__query = session
        
    def get_user_with_id(self):
        print(self.__session)
        query = self.__session.query(Users.firstname).all()
        print(query)
        