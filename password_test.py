import unittest
from user import User
from user import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user and credentials classes behaviours.
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






if __name__ == '__main__':
    unittest.main()
