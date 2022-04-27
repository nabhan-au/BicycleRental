from sqlalchemy import Column, ForeignKey, Text, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

from models.users_model import Users

Base = declarative_base()

class Bicycle(Base):
    __tablename__ = "bicycle"
    
    id = Column(Integer, primary_key = True)
    type = Column(Text, nullable = False)
    brand = Column(Text, nullable = False)
    seat = Column(Integer, default = 1)
    user_id = Column(Integer, ForeignKey(Users.id))
    user = relationship(Users)
    def __repr__(self):
        return f"<User(type={self.type}, brand={self.brand}, seat={self.seat}, user_id={self.user_id})>"