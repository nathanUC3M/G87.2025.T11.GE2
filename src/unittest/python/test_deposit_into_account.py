"""Testing module for the deposit into account method"""
import unittest
import logging
from freezegun import freeze_time
from src.main.python.uc3m_money import AccountManager, AccountManagementException

logging.basicConfig(
    filename=r"\src\unittest\python\test_cases.log",
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
class MyTestCaseAgain(unittest.TestCase):
    """
    Unit test class for testing the Account Manager Class
    Contains test cases related to the derivation tree given
    for the inputs of this class.
    """

    #Test valid hash
    @freeze_time("2025-03-24 17:55:00")
    def test_valid_str(self):
        """
        Tests the successful deposit from a valid JSON file and ensures
        that the correct deposit signature is returned.
        """
        ob_valid = AccountManager()
        check_signature ="cc5f38885ee9362fc670e795e38bbabceada297a436bc05faf7995ebdbeeac6c"
        result = ob_valid.deposit_into_account("test.json")
        self.assertEqual(check_signature, result)

    def test_empty_file(self):
        """
        Tests that the deposit_into_account method raises an
        AccountManagementException when given an empty or non-existent file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test2.txt")


    def test_dup_file(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the provided JSON file has duplicate data.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test3.json")

    def test_delete_1_quote(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the first quotation mark in the JSON file is deleted.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test4.json")

    def test_dup_1_quote(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the first quotation mark in the JSON file is duplicated.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test5.json")

    def test_delete_last_quote(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the last quotation mark in the JSON file is deleted.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test6.json")

    def test_dup_last_quote(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the last quotation mark in the JSON file is duplicated.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test7.json")

    def test_delete_data(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the data section of the JSON file is deleted.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test8.json")

    def test_dup_data(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the data section in the JSON file is duplicated.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test9.json")

    def test_modify_bracket(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the bracket in the JSON file is changed into another symbol.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test10.json")

    def test_delete_1_field(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the IBAN field (1st field) is deleted from the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test11.json")

    def test_dup_1_field(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the IBAN field (1st field) is duplicated in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test12.json")

    def test_delete_sep(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the separator (the comma) in the JSON file is deleted.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test13.json")

    def test_dup_sep(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the separator (the comma) in the JSON file is duplicated.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test14.json")

    def test_delete_2_field(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the second field (amount) in the JSON file is deleted.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test15.json")

    def test_dup_2_field(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the second field (amount) in the JSON file is duplicated.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test16.json")

    def test_modify_end_bracket(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the closing bracket in the JSON file is modified to symbol.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test17.json")

    def test_delete_1_label(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the first label (IBAN) in the JSON file is deleted.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test18.json")

    def test_dup_1_label(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the first label (IBAN) in the JSON file is duplicated.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test19.json")

    def test_delete_equals(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when an equals sign (between the fields) is deleted from the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test20.json")

if __name__ == '__main__':
    unittest.main()
