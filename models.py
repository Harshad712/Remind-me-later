from pydantic import BaseModel, Field
from datetime import date, time
from enum import Enum

class RemindMethod(str, Enum):
    sms = "sms"
    email = "email"

class Reminder(BaseModel):
    date: date
    time: time
    message: str = Field(..., min_length=1)
    remind_by: RemindMethod
