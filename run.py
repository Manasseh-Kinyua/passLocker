#!/usr/bin/env python3.9
from user import User
from user import Credentials

def logo():
	print("    ____                         _                   _                         ")
	print("   |  _ \                       | |                 | |  /\                    ")
	print("   | |_) )  ____  ___   ___     | |      _____  _ _ | | / /   ____    _ _      ")
	print("   |  __/  / _  |/ __  / __     | |     /  _  \| '_|| |/ /   / __  \ |  _|     ")
	print("   | |    / (_| |\__ \ \__ \    | |___ (  (_)  ) |_ | | \ \  |  ___/ | |       ")
	print("   |_|    \_____| ___/  ___/    |_____) \_____/|____| |  \_\  \____  |_|       ")
logo()

def create_new_user(username, password):
    '''
    Function to create a new user
    '''
    new_user = User(username, password)
    return new_user

def save_users(user):
    '''
    Function to save new users.
    '''
    user.save_user()

def display_user():
    '''
    Function to display users in the user list.
    '''
    return user.display_users()

def login_user(username, password):
    '''
    Function that checks if a user exists, and logs them in.
    '''
    check_user = Credentials.verify_user(username, password)
    return check_user

def create_new_credential(account, userName, password):
    '''
    Functon to create new credentials for a user.
    '''
    new_credential = Credentials(account, userName, password)
    return new_credential

def save_credentials(credentials):
    '''
    Function that saves user credentials to the credentials list.
    '''
    credentials.save_credential()

def display_credential():
    '''
    Function to display the saved user credentials.
    '''
    return Credentials.display_credentials()
    
















# if __name__ == '__main__':
#     main()
