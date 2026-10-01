from datetime import date, timedelta
from database import SessionLocal, engine, Base
import models

#creates the tables in the database if they don't already exist
Base.metadata.create_all(engine)
db = SessionLocal()

#records the current date and creates a quest that starts today and ends in 6 days,(lasts 7 days) then adds it to the database
today = date.today()
quest = models.Quest(title="Arrays Week", week_start=today, week_end=today + timedelta(days=6))
db.add(quest)
db.commit()
db.refresh(quest)

#creates a list of tasks that are associated with the quest and adds them to the database
tasks = [
    models.Task(quest_id=quest.id, title="Two Sum", url="https://leetcode.com/problems/two-sum/", kind="coding", xp_value=10),
    models.Task(quest_id=quest.id, title="Contains Duplicate", url="https://leetcode.com/problems/contains-duplicate/", kind="coding", xp_value=10),
    models.Task(quest_id=quest.id, title="Write one STAR story about a time you led", kind="behavioral", xp_value=20),
    models.Task(quest_id=quest.id, title="Research 5 employers that have sponsored H-1Bs", kind="career", xp_value=20),
]
#saves them all at once to the database and closes the session
db.add_all(tasks)
db.commit()
db.close()
print("Starter Pack Created ", quest.title)