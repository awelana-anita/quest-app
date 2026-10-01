from fastapi import FastAPI
from database import engine, Base, SessionLocal
from pydantic import BaseModel
import models

#create_all builds the tables in the database if they don't already exist
Base.metadata.create_all(engine)

#creates the application object that will be used to define the routes and run the server 
app = FastAPI()

class UserCreate(BaseModel):
    email: str
    display_name: str
    xp: int = 0



@app.get("/")
def home_root():
    return {"message": "Quest App is running!"}


#post: means someone is sending data to the server
#to register a user, we will create a post request that takes in the user data and adds it to the database
@app.post("/register")
def register_user(user: UserCreate):
    db = SessionLocal()
    #create a new user object from the data provided in the request
    new_user = models.User(email=user.email, display_name=user.display_name, xp=user.xp)
    #adds the new user to the database
    db.add(new_user)
    db.commit()
    #check that the user was added to the database and return a success message
    db.refresh(new_user)
    db.close()
    return {"message": "User registered successfully", "user_id": new_user.id, "email": new_user.email, "display_name": new_user.display_name, "xp": new_user.xp
        }

#get: means that we have to get data from the server
#to get a user by their id, we will create a get request that takes in the user id and returns the user data
@app.get("/user/{user_id}")
def get_user(user_id: int):
    db = SessionLocal()
    #query the database for the user with the given id
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.close()
    if user:
        return {"user_id": user.id, "email": user.email, "display_name": user.display_name, "xp": user.xp}
    else:
        return {"message": "User not found"}
