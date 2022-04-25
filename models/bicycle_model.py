from sqlalchemy import Column, Text, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Bicycle(Base):
    __tablename__ = "bicycle"
    
    id = Column(Integer, primary_key = True)
    type = Column(Text, nullable = False)
    brand = Column(Text, nullable = False)
    seat = Column(Integer, default = 1)
    user_id = Column(Integer, nullable = False)
    
    def __repr__(self):
        return f"<User(type={self.type}, brand={self.brand}, seat={self.seat}, user_id={self.user_id})>"