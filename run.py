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















# if __name__ == '__main__':
#     main()
