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

    def __init__(self, username, password):
        self.username = username
        self.password = password



class Credentials:
    '''
    Class that generates credentials for each user.
    '''

    credentials_list = []

    def __init__(self, account, userName, password):
        self.account = account
        self.userNmae = username
        self.password = password
