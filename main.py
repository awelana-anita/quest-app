from fastapi import FastAPI
from database import engine, Base
import models

#create_all builds the tables in the database if they don't already exist
Base.metadata.create_all(engine)

#creates the application object that will be used to define the routes and run the server 
app = FastAPI()

@app.get("/")
def home_root():
    return {"message": "Quest App is running!"}