import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL", "sqlite:///./prepquest.db"))
#makes a session that will be used to interact with the database
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
