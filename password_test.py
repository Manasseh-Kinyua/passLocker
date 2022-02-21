import unittest
from user import User
from user import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user and class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('NassehKinyua', 'nasseh82')

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_user.username,'NassehKinyua')
        self.assertEqual(self.new_user.password,'nasseh82')

    def test_save_user(self):
        '''
        Test case to check if new instances of the user object are added to the user list.
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we ca save multiple user objects to our user_list.
        '''
        self.new_user.save_user()
        test_user = User('TestName', '12345678')
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        Method to check if we can remove a user from the user list.
        '''
        self.new_user.save_user()
        test_user = User('TestName', '12345678')
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_display_all_users(self):
        '''
        Return a list of all users saved.
        '''
        self.assertEqual(User.display_users(), User.user_list)


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials('Gmail', 'Nasseh_Kinyua', 'nasseh73')

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_credential.account, 'Gmail')
        self.assertEqual(self.new_credential.userName, 'Nasseh_Kinyua')
        self.assertEqual(self.new_credential.password, 'nasseh73')

    def test_save_credential(self):
        '''
        Test case to check if new instances of the credentials object are added to the credentials list.
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_miltiple_credentials(self):
        '''
        Test case to check if miltiple details can be added to the credentials list.
        '''
        self.new_credential.save_credential()
        test_credential = Credentials('Facebook', 'GeorgeKiny', 'xyz12345')
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        '''
        Test case to check that a user can delete a credential object.
        '''
        self.new_credential.save_credential()
        test_credential = Credentials('Facebook', 'GeorgeKiny', 'xyz12345')
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credential_by_account(self):
        '''
        Test case to verify that we can find an credentials object using its acount name.
        '''
        self.new_credential.save_credential()
        test_credential = Credentials('Facebook', 'GeorgeKiny', 'xyz12345')
        test_credential.save_credential()

        found_credential = Credentials.find_by_account('Facebook')
        self.assertEqual(found_credential.account, test_credential.account)

    def test_credential_exists(self):
        '''
        test to check if we can return a boolean if we cannot find the credential.
        '''
        self.new_credential.save_credential()
        test_credential = Credentials('Facebook', 'GeorgeKiny', 'xyz12345')
        test_credential.save_credential()

        credential_exists = Credentials.credential_exist('Facebook')
        self.assertTrue(credential_exists)









if __name__ == '__main__':
    unittest.main()
