from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


#keep my data in a file called questapp.db
engine = create_engine("sqlite:///questapp.db")
Base = declarative_base()



