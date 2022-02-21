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

def del_credential(credentials):
    '''
    Functon to delete a credentials object.
    '''
    credentials.delete_credential()

def find_credential(account):
    '''
    Function that checks if a credential object is in the credentials class.
    '''
    return Credentials.find_by_account(account)

def generate_password():
    '''
    Functionthat generates an aotomatic password for the user if they choose that option.
    '''
    generated_pass = Credentials.generatePassword()
    return generated_pass

def copy_password(account):
    '''
    Function that copies a user's password to the clipboard.
    '''
    return Credentials.copy_password(account)


def main():
    print("Hello, Welocome to Pass Locker. We are a store for your Accounts Passwords.....\n Please ENTER one of the following short codes to proceed.\n 'cr' -> Create a New Account. \n 'h1' -> Already have an Account. \n")
    short_code = input().lower().strip()
    if short_code == 'cr':
        print("Please Sign Up")
        print('*' * 50)
        username = input("Enter your username: ")

        while True:
            print("Please USE one of the followig to enter your own password or to have one selected for you.\n 'em' -> To enter own password.\n 'ap' -> To have an automatic password generated for you.\n")
            choice = input().lower().strip()
            if choice == 'em':
                password = input("Please enter your password; ")
                break
            elif choice == 'ap':
                password = generate_password()
            else:
                print("Invalid passwordchoice......Please try again with a correct choice.")
                save_users(create_new_user(username, password))
                print("8" * 85)
                print(f"Hello {username}, You have created an account successfully.\n Your password id : {password}")
                print("8" * 85)

    elif short_code == 'h1':
        

















if __name__ == '__main__':
    main()
