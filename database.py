from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL, server_api=ServerApi("1"), connectTimeoutMS=50000)

db = client["Remainders"]
reminders_db = db["remainders"]
