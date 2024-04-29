from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

from Kisan import DB_NAME, MONGO_DB_URI

mongo = MongoClient(MONGO_DB_URI)
dbname = mongo[DB_NAME]
