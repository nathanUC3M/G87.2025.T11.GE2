"""Testing module for the deposit into account method"""
import unittest
import logging
from src.main.python.uc3m_money import AccountManager, AccountManagementException

logging.basicConfig(
    filename=r"\src\unittest\python\test_cases.log",
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
class MyTestCase3(unittest.TestCase):
    """
    Unit test class for testing the Account Manager Class
    Contains test cases related to the derivation tree given
    for the inputs of this class.
    """
    def test_dup_decimal(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the decimal place is duplicated in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test41.json")

    def test_modify_decimal(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the decimal place is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test42.json")

    def test_delete_after_decimal(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the number after the decimal point is deleted in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test43.json")

    def test_dup_after_decimal(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the number after the decimal point is duplicated in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test44.json")

    def test_modify_value_after_decimal(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the number after the decimal point is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test45.json")

    def test_modify_quotation_value_2(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the quotation mark before the second value is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test46.json")

    def test_modify_quotation_after_v2(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the quotation mark after the second value is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test47.json")

    def test_modify_eur_content(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the "EUR" currency content is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test48.json")

    def test_modification_equal_field_2(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the equal sign in the second field is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test49.json")

    def test_modify_quotation_before_l1(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the quotation mark before label 1 is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test50.json")

    def test_modify_l1(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when label 1 is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test51.json")

    def test_modify_quotation_after_l1(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the quotation mark after label 1 is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test52.json")

    def test_modify_quotation_before_v1(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the quotation mark before value 1 is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test53.json")

    def test_modify_country_code(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the IBAN country code is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test54.json")

    def test_modify_iban_num(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the IBAN numbers are modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test55.json")

    def test_modify_quotation_before_l2(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the quotation mark before label 2 is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test56.json")

    def test_modify_quotation_after_v1(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the quotation mark after value 1 is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test57.json")

    def test_modify_amount(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the "AMOUNT" field is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test58.json")

    def test_modify_quote_after_l2(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the quotation mark after label 2 is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test59.json")

if __name__ == '__main__':
    unittest.main()
