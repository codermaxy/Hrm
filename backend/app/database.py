import os
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import certifi

load_dotenv()

# Match the variable name in .env
MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME", "hrms_lite")

# Use certifi for SSL CA bundle
client = AsyncIOMotorClient(MONGODB_URL, tlsCAFile=certifi.where())
db = client[DATABASE_NAME]

async def get_database():
    return db
