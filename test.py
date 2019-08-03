from unittest import mock
from unittest import TestCase
import unittest
import main_for_test


class LoginTest(TestCase):

    '''
    tests user
    '''
    @mock.patch('main_for_test.input', create=True)
    def testsignup(self, mocked_input):
        mocked_input.side_effect = ['test_user', '1234']
        result = main_for_test.signup()
        self.assertEqual(result, 'test_user')
    
    '''
    tests login success
    '''
    @mock.patch('main_for_test.input', create=True)
    def testloginSuccess(self, mocked_input):
        mocked_input.side_effect = ['new_user', '1234']
        result = main_for_test.login()
        self.assertEqual(result, 'new_user')

    '''
    tests journal entry
    '''
    @mock.patch('main_for_test.input', create=True)
    def testjournalentry(self, mocked_input):
        mocked_input.side_effect = ['journal entry']
        result = main_for_test.journal_entry('new_user')
        self.assertEqual(result, True)

    '''
    tests login failed with new user
    '''
    @mock.patch('main_for_test.input', create=True)
    def testloginFail(self, mocked_input):
        mocked_input.side_effect = ['---', '123']
        result = main_for_test.login()
        self.assertEqual(result, False)

    

unittest.main()