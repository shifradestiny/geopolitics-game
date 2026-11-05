from pymongo import MongoClient
import certifi
from werkzeug.security import generate_password_hash, check_password_hash

MONGO_URI = "mongodb+srv://game-admin:24680@geopoliticscluster.co7orwl.mongodb.net/"

class Database:
    def __init__(self):
        try:
            self.client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
            self.db = self.client["geopolitics_db"]

            self.users = self.db["users"]
            self.games = self.db["games"]
            print("Successfully connected to MongoDB Atlas!")
        except Exception as e:
            print(f"Database connection error, {e}")

    # Authentication
    def register_user(self, username, password):
        if self.users.find_one({"username": username}):
            return False 

        hashed_password = generate_password_hash(password)
        self.users.insert_one({"username": username, "password": hashed_password})
        return True

    def verify_user(self, username, password):
        user = self.users.find_one({"username": username})
        if user and check_password_hash(user["password"], password):
            return True
        return False

    # Game State Logic
    def save_game_state(self, username, game_data):
        self.games.update_one(
            {"username": username},
            {"$set": {
                "game_data": game_data
            }},
            upsert=True 
        )
        return True

    def load_game_state(self, username):
        game = self.games.find_one({"username": username})
        if game:
            return game.get("game_data")
        return None

db = Database()