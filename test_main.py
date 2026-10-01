import os
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

from fastapi.testclient import TestClient
from main import app

#pretend browser to talk to my application and test the routes
client = TestClient(app)

#this test checks that the home route returns a 200 status code and the correct message
def test_home_root():
    #visits the front page
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Quest App is running!"}

#this test checks that a user can be registered and that the correct data is returned 
def test_register_user():
    response = client.post("/register", json={"email": "a@test.com", "display_name": "testuser", "xp": 10})
    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"
    assert response.json()["email"] == "a@test.com"
    assert response.json()["display_name"] == "testuser"
    assert response.json()["xp"] == 10
