# user_management.py
import json
import bcrypt
import os

# Path to the user data file
user_data_file = 'user_data.json'

def load_user_data():
    if not os.path.exists(user_data_file):
        return {}
    with open(user_data_file, 'r') as file:
        return json.load(file)

def save_user_data(data):
    with open(user_data_file, 'w') as file:
        json.dump(data, file, indent=4)

def register_user():
    users_data = load_user_data()
    username = input("Choose a username: ")
    if username in users_data:
        print("Username already taken. Please choose a different one.")
        return register_user()
    password = input("Choose a password: ")
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users_data[username] = {'password': hashed.decode('utf-8'), 'level': 1}
    save_user_data(users_data)
    print("Registration successful!")

def login_user():
    users_data = load_user_data()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user_data = users_data.get(username)
    if user_data and bcrypt.checkpw(password.encode('utf-8'), user_data['password'].encode('utf-8')):
        print(f"Welcome back, {username}! You are in Level {user_data['level']}.")
        return username, user_data['level']
    else:
        print("Invalid username or password.")
        return None, None
def record_language_choice(username, language):
    users_data = load_user_data()
    if username in users_data:
        users_data[username]['last_language'] = language
        save_user_data(users_data)

def get_user_level(username):
    users_data = load_user_data()
    return users_data.get(username, {}).get('level', 1)
def update_user_level(username, new_level):
    users_data = load_user_data()
    if username in users_data:
        users_data[username]['level'] = new_level
        save_user_data(users_data)
