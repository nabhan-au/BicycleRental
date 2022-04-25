from sqlalchemy import Column, Text, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True)
    firstname = Column(Text, nullable = False)
    lastname = Column(Text, nullable = False)
    age = Column(Integer, nullable = False)
    
    def __repr__(self):
        return f"<User(firstname={self.firstname}, lastname={self.lastname}, age={self.age})>"