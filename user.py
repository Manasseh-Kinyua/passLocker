import random
import pyperclip
import string

class User:
    '''
    Class that generates new instances of a user.
    '''

    user_list = []

    def save_user(self):
        '''
        Method that saves user instances to the user list.
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        Method that removes a user instance from the user list.
        '''
        User.user_list.remove(self)

    @classmethod
    def display_users(cls):
        '''
        Method that returns the user list.
        '''
        return cls.user_list

    def __init__(self, username, password):
        self.username = username
        self.password = password



class Credentials:
    '''
    Class that generates credentials for each user.
    '''

    credentials_list = []

    def save_credential(self):
        '''
        Method to add new credential objects to the credentials list.
        '''
        Credentials.credentials_list.append(self)

    def delete_credential(self):
        '''
        Method that removes a credentials object from the credentials list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_account(cls, account):
        '''
        method that takes an account and returns a credential that matches that account.
        Args:
            account: account name to search for
        Returns:
            Credentials of object that matches the account
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def credential_exist(cls, account):
        '''
        Method that checks if a credential exists and returns either True or False.
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    def generatePassword(stringLength = 8):
        '''
        Method to generate a random 8-character password for the user.
        '''
        password = string.ascii_uppercase + string.ascii_lowercase +string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))


    def __init__(self, account, userName, password):
        self.account = account
        self.userName = userName
        self.password = password
