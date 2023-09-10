# app/models/user.py

from app import mongo

class User:
    def __init__(self, username, password, phone):
        self.username = username
        self.password = password
        self.phone = phone

    @staticmethod
    def find_by_username(username):
        return mongo.db.Users.find_one({"username": username})

    @staticmethod
    def create(username, password, phone):
        user_data = {
            "username": username,
            "password": password,
            "phone": phone
        }
        mongo.db.Users.insert_one(user_data)

    def update(username, password=None, phone=None):
        user = User.find_by_username(username)
        if not user:
            return False

        if password:
            user['password'] = password
        if phone:
            user['phone'] = phone

        # Update the user in the database
        mongo.db.Users.update_one({"username": username}, {"$set": user})
        return True


     