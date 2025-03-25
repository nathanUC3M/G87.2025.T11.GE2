"""Testing module for the deposit into account method"""
import unittest
from src.main.python.uc3m_money import AccountManager, AccountManagementException

class MyTestCase2(unittest.TestCase):
    """
    Unit test class for testing the Account Manager Class
    Contains test cases related to the derivation tree given
    for the inputs of this class.
    """
    def test_dup_equal(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when an equals sign (between the fields) is duplicated in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test21.json")

    def test_delete_value_1(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the first value (iban number) in the JSON file is deleted.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test22.json")

    def test_dup_value_1(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the first value (iban number) in the JSON file is duplicated.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test23.json")

    def test_modify_separator(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the equals sign in the JSON file is modified.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test24.json")

    def test_delete_label_2(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the second label (AMOUNT) in the JSON file is deleted.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test25.json")

    def test_dup_label_two(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the second label (AMOUNT) in the JSON file is duplicated.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test26.json")

    def test_delete_equal_again(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the equals sign in the second field (the amount) of the JSON file is deleted.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test27.json")

    def test_dup_equal_again(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the equals sign in the second field (the amount) of the JSON file is duplicated.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test28.json")

    def test_delete_second_value(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the second value (euros) in the JSON file is deleted.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test29.json")

    def test_duplicate_second_value(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the second value (euros) in the JSON file is duplicated.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test30.json")

    def test_modification_equal_label_1(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the equals sign in the first label is modified.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test31.json")

    def test_delete_iban_num(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the IBAN number in the JSON file is deleted.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test32.json")

    def test_dup_iban_num(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the IBAN number in the JSON file is duplicated.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test33.json")

    def test_delete_eur(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the currency identifier "EUR " is deleted from the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test34.json")

    def test_dup_eur(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the currency identifier "EUR " is duplicated in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test35.json")

    def test_modify_eur(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the currency identifier "EUR " is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test36.json")

    def test_delete_before_decimal_num(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the number before the decimal point is deleted in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test37.json")

    def test_dup_before_decimal_num(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the number before the decimal point is duplicated in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test38.json")

    def test_modify_num_before_decimal(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the number before the decimal point is modified in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test39.json")

    def test_delete_decimal(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the decimal place is deleted in the JSON file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test40.json")

if __name__ == '__main__':
    unittest.main()
