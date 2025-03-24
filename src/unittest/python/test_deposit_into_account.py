
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

    #Test empty file (delete file)
    def test_empty_file(self):
        """
        Tests that the deposit_into_account method raises an
        AccountManagementException when given an empty or non-existent file.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test2.txt")


    #Test duplicated file
    def test_dup_file(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the provided JSON file has duplicate data.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test3.json")

    #Test deleting first quotation
    def test_delete_1_quote(self):
        """
        Tests that the deposit_into_account method raises an AccountManagementException
        when the first quotation mark in the JSON file is deleted.
        """
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test4.json")

    # Test duplicating first quotation
    def test_dup_1_quote(self):

        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test5.json")

    # Test deleting last quotation
    def test_delete_last_quote(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test6.json")

    # Test duplicating last quotation
    def test_dup_last_quote(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test7.json")

    # Test deleting the data
    def test_delete_data(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test8.json")

    # Test duplicating the data
    def test_dup_data(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test9.json")

    # Test modifying the bracket
    def test_modify_bracket(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test10.json")

    # Test deleting IBAN field
    def test_delete_1_field(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test11.json")

    # Test duplicating IBAN filed
    def test_dup_1_field(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test12.json")

    # Test deleting separator
    def test_delete_sep(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test13.json")

    # Test duplicating separator
    def test_dup_sep(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test14.json")

    # Test delete second field
    def test_delete_2_field(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test15.json")

    # Test duplicating second field
    def test_dup_2_field(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test16.json")

    # Test modifying end bracket
    def test_modify_end_bracket(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test17.json")

    # Test delete first label
    def test_delete_1_label(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test18.json")

    # Test duplicate first label
    def test_dup_1_label(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test19.json")

    # Test delete equals sign
    def test_delete_equals(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test20.json")

    # Test duplicating equal sign
    def test_dup_equal(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test21.json")

    # Test delete value one
    def test_delete_value_1(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test22.json")

    # Test duplicate value one
    def test_dup_value_1(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test23.json")

    # Modify the separator
    def test_modify_separator(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test24.json")

    # Test delete label two
    def test_delete_label_2(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test25.json")

    # Test duplicate label two
    def test_dup_label_two(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test26.json")

    # Test delete equal in second field
    def test_delete_equal_again(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test27.json")

    # Test duplicate equal in second field
    def test_dup_equal_again(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test28.json")

    # Test delete second value
    def test_delete_second_value(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test29.json")

    # Test duplicate second value
    def test_duplicate_second_value(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test30.json")

    # Test modification of the equal sign
    def test_modification_equal_label_1(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test31.json")

    # Test delete the IBAN number
    def test_delete_iban_num(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test32.json")

    # Test duplicate IBAN number
    def test_dup_iban_num(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test33.json")

    # Test delete "EUR "
    def test_delete_eur(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test34.json")

    # Test duplicate "EUR "
    def test_dup_eur(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test35.json")

    # Test modify "EUR "
    def test_modify_eur(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test36.json")

    # Test delete number before decimal
    def test_delete_before_decimal_num(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test37.json")

    # Test duplicate number before decimal
    def test_dup_before_decimal_num(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test38.json")

    # Test modify value before decimal
    def test_modify_num_before_decimal(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test39.json")

    # Test delete decimal place
    def test_delete_decimal(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test40.json")

    # Test duplicate decimal place
    def test_dup_decimal(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test41.json")

    # Test modify decimal place
    def test_modify_decimal(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test42.json")

    # Test delete value after decimal
    def test_delete_after_decimal(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test43.json")

    # Test duplicate value after decimal
    def test_dup_after_decimal(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test44.json")

    # Test modify value after decimal
    def test_modify_value_after_decimal(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test45.json")

    # Test modify quotation before value 2
    def test_modify_quotation_value_2(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test46.json")

    # Test modify quotation after value 2
    def test_modify_quotation_after_v2(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test47.json")

    # Test modify "EUR"
    def test_modify_eur_content(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test48.json")

    # Test modify equal field 2
    def test_modification_equal_field_2(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test49.json")

    # Test modify quotation before label 1
    def test_modify_quotation_before_l1(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test50.json")

    # Test modify label 1
    def test_modify_l1(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test51.json")

    # Test modify quote after label 1
    def test_modify_quotation_after_l1(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test52.json")

    # Test modify quotation before value 1
    def test_modify_quotation_before_v1(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test53.json")

    # Test modify IBAN country code
    def test_modify_country_code(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test54.json")

    # Test modify IBAN numbers
    def test_modify_iban_num(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test55.json")

    # Test modify quotation before label 2
    def test_modify_quotation_before_l2(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test56.json")

    # Test modify quotation after value 1
    def test_modify_quotation_after_v1(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test57.json")

    # Test modify AMOUNT
    def test_modify_AMOUNT(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test58.json")

    # Test modify quotation after label 2
    def test_modify_quote_after_l2(self):
        ob_invalid = AccountManager()
        with self.assertRaises(AccountManagementException):
            ob_invalid.deposit_into_account("test59.json")


if __name__ == '__main__':
    unittest.main()
