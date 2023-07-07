import json
import re
import random
def save_user_data(users):
    with open("users_data.json", "w") as file:
        json.dump(users, file)


def sign_up():
   
    
    pattern = r"^(?=.*[A-Z])[a-zA-Z]{4,8}$"
    
    user_name_pattern = r'^[a-zA-Z0-9_]{3,20}$'
    
    try:
        with open("users_data.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}

    
    while True:
        username = input("Enter a username: ")
        if username in users:
            
            print("Username already exists. Please try again.")
            continue
        elif re.match(user_name_pattern, username):
            break
        print("invalid username pattern, note: no space")

      
        
            
    while True:
        password = input("Enter a password (4-8 characters, at least one uppercase): ")
        if re.match(pattern, password):
            break
        print("Invalid password pattern. Please try again.")

     

    users[username] = password

    save_user_data(users)
    print(" You have successful sign up.")
   

def sign_in():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Load existing user data from JSON file
    user_data = load_user_data()

    # Check if username exists and password matches
    if username in user_data and user_data[username] == password:
        print("Sign in successful!")
    else:
        print("Invalid username or password. Please try again.")


def load_user_data():
    try:
        with open('users_data.json') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}
    return user_data

def save_user_data(user_data):
    with open('users_data.json', 'w') as file:
        json.dump(user_data, file)

# Main program
while True:
    print("1. Sign Up")
    print("2. Sign In")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        sign_up()
    elif choice == '2':
        sign_in()
    
        break
    else:
        print("Invalid choice. Please try again.")
