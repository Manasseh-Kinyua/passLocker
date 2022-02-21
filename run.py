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
        print("*" * 50)
        print("Please ENTER username and password to login...")
        print("*" * 50)
        username = input("Enter username:")
        password = input("Enter password:")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}, Welcome to Pass Locker")
            print('\n')

    while True:
        print("Please use the following short codes.\n crc -> To creatte new credentials.\n dc -> To display credentials.\n fc -> To find credentials.\n gp -> To generate new credentials.\n d -> To delete credentials. \n ex -> To exit the application.\n")
        short_code = input().lower().strip()
        if short_code == 'crc':
            print("Create new credentials")
            print("." * 20)
            print("Enter Account Name....")
            account = input().lower()
            print("Enter the account username")
            userName = input()

            while True:
                print("Choose: em -> to enter your own password.\n ap -> To have a password generated for you.\n")
                choice = input().lower().strip()
                if choice == 'em':
                    password = input("Please enter your password: \n")
                    break
                elif choice == 'ap':
                    password = generate_password()
                    break
                else:
                    print("Invalid choice....PLease try again with the correct choice.")
                    save_credentials(create_new_credential(account, userName, password))
                    print('\n')
                    print(f"Credentials for {account} have been created")
                    print('\n')

        elif short_code == 'dc':
            if display_credential():
                print("Here is a list of your credentials:")
                print("*" * 30)
                print("_" * 30)

                for credential in display_credential():
                    print(f"Account: {credential.account}\n UserName: {credential.userName}\n password: {credential.password}")
                    print("_" * 30)
                print("*" * 30)
            else:
                print("You do not have aby credentials saved yet.....")

        elif short_code == 'fc':
            print("Please enter the account you want to find")
            search_acc = input().lower()
            if find_credential(search_acc):
                search_credential = find_credential(search_acc)
                print(f"Account: {search_credential.account}")
                print("-" * 50)
                print(f"userName: {search_credential.userName}\n Password: {search_credential.password}")
                print("-" * 50)
            else:
                print("The name you entered is not an account name in available credentials")
                print('\n')

        elif short_code == 'd':
            print("Enter the Account for the credential you want to delete")
            search_acc = input().lower()
            if find_credential(search_acc):
                search_credential = find_credential(search_acc)
                search_credential.del_credential()
                print('\n')
                print(f"{search_credential.account} has been successfully deleted!")
                print('\n')
            else:
                print("The name you entered does not match any in our list")

        elif short_code == 'gp':
            password = generate_password()
            print(f"{password} Generated successfully. Proceed to use it.")
        elif short_code == 'ex':
            print("Thank you for using Pass Locker....See you another time...BYE.....")
            break
        else:
            print("Wrong entry....PLease use the short codes provided")

    else:
        print("Please always enter a valid input in order to use the application.")

if __name__ == '__main__':
    main()
