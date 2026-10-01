# quest-app

A gamified interview-prep app. Small private groups complete weekly
quests (coding, behavioral, and career tasks), earn XP, and keep streaks.

**Status:** in progress

## Built so far
- REST API with FastAPI and SQLAlchemy
- User registration with duplicate-email check
- Automated tests with pytest

## Run it
    pip install -r requirements.txt
    uvicorn main:app --reload

## Run the tests
    pytest

## Coming next
Login, private groups, XP and streaks, frontend, deployment.