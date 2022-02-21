class User:
    '''
    Class that generates new instances of a user.
    '''

    user_list = []

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
