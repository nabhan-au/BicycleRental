from sqlalchemy import Column, ForeignKey, Text, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from models.users_model import Users

Base = declarative_base()

class Bicycle(Base):
    """Model of bicycle class.

    Args:
        id(int): unqiue id of bicycle.
        type(str): type of bicycle.
        brand(str): brand of bicycle.
        seat(int): number of seats in that bicycle.
        user_id(int): id of user who rent the bicycle.
        user(Users): user model.

    Returns:
        str: information of bicycle class.
    """
    __tablename__ = "bicycle"
    
    id = Column(Integer, primary_key = True)
    type = Column(Text, nullable = False)
    brand = Column(Text, nullable = False)
    seat = Column(Integer, default = 1)
    user_id = Column(Integer, ForeignKey(Users.id))
    user = relationship(Users)
    def __repr__(self):
        return f"<User(type={self.type}, brand={self.brand}, seat={self.seat}, user_id={self.user_id})>"