# user.py - Create this new file to define the User class

from flask_login import UserMixin
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["db"]

class User(UserMixin):
    def __init__(self, user_id, username):
        self.id = user_id  # The user ID is the ObjectId from MongoDB
        self.username = username  # The user's username from MongoDB

# This method is used by Flask-Login to load a user from the database by their ID.
def load_user(user_id):
    user_data = db["users"].find_one({"_id": ObjectId(user_id)}) # Replace "db" with your actual database name, Assuming users collection is called 'users'
    if user_data:
        return User(str(user_data["_id"]), user_data["username"])
    return None



