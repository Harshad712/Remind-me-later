from fastapi import FastAPI
from fastapi import HTTPException
from models import Reminder
from database import reminders_db
import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/reminders/")
async def create_reminder(reminder: Reminder):
    reminder_dict = reminder.dict()
    
    # Combine date and time into a datetime object
    combined_datetime = datetime.datetime.combine(
        reminder_dict["date"],
        reminder_dict["time"]
    )
    
    # Check if reminder is in the past
    if combined_datetime < datetime.datetime.utcnow():
        raise HTTPException(status_code=400, detail="Cannot set a reminder in the past.")
    
    reminder_dict["remind_at"] = combined_datetime
    reminder_dict["created_at"] = datetime.datetime.utcnow()

    # Remove separate date and time keys before inserting
    del reminder_dict["date"]
    del reminder_dict["time"]

    result = await reminders_db.insert_one(reminder_dict)
    return {
        "id": str(result.inserted_id),
        "status": "Reminder saved!"
    }
    
    
@app.get("/reminders/")
async def get_all_reminders():
    reminders = []
    cursor = reminders_db.find()
    async for r in cursor:
        r["id"] = str(r["_id"])
        r["date"] = r["remind_at"].date()
        r["time"] = r["remind_at"].time()
        del r["_id"]
        reminders.append(r)
    return reminders

