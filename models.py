from sqlalchemy import Column, Integer, String
from database import Base

#create a table user with four columns

class User(Base):
    __tablename__= "users"
    #their identifier
    id = Column(Integer, primary_key = True)
    #their email
    email = Column(String)
    #their username
    display_name = Column(String)
    #their xp
    xp = Column(Integer, default = 0)