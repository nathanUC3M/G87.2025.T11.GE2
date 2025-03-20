import unittest

from src.main.python.uc3m_money import AccountManager
from src import JsonFiles


class MyTestCaseAgain(unittest.TestCase):


    #Test valid hash
    def test_valid_ST(self):
        ob_valid = AccountManager()
        result = ob_valid.deposit_into_account("test.json")
        self.assertEqual(result, "placeholder")
        # add assertion here

    #Test empty file (delete file)
    def test_empty_file(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test2.json")
        result.assertThrows("The file is not in JSON format")

    #Test duplicated file
    def test_dup_file(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test3.json")
        result.assertThrows("The file is not in JSON format")

    #Test deleting first quotation
    def test_delete_1_quote(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test4.json")
        result.assertThrows("The file is not in JSON format")

    # Test duplicating first quotation
    def test_dup_1_quote(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test5.json")
        result.assertThrows("The file is not in JSON format")

    # Test deleting last quotation
    def test_delete_last_quote(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test6.json")
        result.assertThrows("The file is not in JSON format")

    # Test duplicating last quotation
    def test_dup_last_quote(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test7.json")
        result.assertThrows("The file is not in JSON format")

    # Test deleting the data
    def test_delete_data(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test8.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test duplicating the data
    def test_dup_data(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test9.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test modifying the bracket
    def test_modify_bracket(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test10.json")
        result.assertThrows("The file is not in JSON format")

    # Test deleting IBAN field
    def test_delete_1_field(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test11.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test duplicating IBAN filed
    def test_dup_1_field(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test12.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test deleting separator
    def test_delete_sep(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test13.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test duplicating separator
    def test_dup_sep(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test14.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test delete second field
    def test_delete_2_field(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test15.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test duplicating second field
    def test_dup_2_field(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test16.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test modifying end bracket
    def test_modify_end_bracket(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test17.json")
        result.assertThrows("The file is not in JSON format")

    # Test delete first label
    def test_delete_1_label(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test18.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test duplicate first label
    def test_dup_1_label(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test19.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test delete equals sign
    def test_delete_equals(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test20.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test duplicating equal sign
    def test_dup_equal(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test21.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test delete value one
    def test_delete_value_1(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test22.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test duplicate value one
    def test_dup_value_1(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test23.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Modify the separator
    def test_modify_separator(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test24.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test delete label two
    def test_delete_label_2(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test25.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test duplicate label two
    def test_dup_label_two(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test26.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test delete equal in second field
    def test_delete_equal_again(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test27.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test duplicate equal in second field
    def test_dup_equal_again(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test28.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test delete second value
    def test_delete_second_value(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test29.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test duplicate second value
    def test_duplicate_second_value(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test30.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test modification of the equal sign
    def test_modification_equal_label_1(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test31.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test delete the IBAN number
    def test_delete_IBAN_num(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test32.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test duplicate IBAN number
    def test_dup_IBAN_num(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test33.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test delete "EUR "
    def test_delete_EUR(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test34.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test duplicate "EUR "
    def test_dup_EUR(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test35.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test modify "EUR "
    def test_modify_EUR(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test36.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test delete number before decimal
    def test_delete_before_decimal_num(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test37.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test duplicate number before decimal
    def test_dup_before_decimal_num(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test38.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test modify value before decimal
    def test_modify_num_before_decimal(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test39.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test delete decimal place
    def test_delete_decimal(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test40.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test duplicate decimal place
    def test_dup_decimal(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test41.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test modify decimal place
    def test_modify_decimal(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test42.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test delete value after decimal
    def test_delete_after_decimal(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test43.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test duplicate value after decimal
    def test_dup_after_decimal(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test44.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test modify value after decimal
    def test_modify_value_after_decimal(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test45.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test modify quotation before value 2
    def test_modify_quotation_value_2(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test46.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test modify quotation after value 2
    def test_modify_quotation_after_v2(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test47.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test modify "EUR"
    def test_modify_EUR_content(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test48.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test modify equal field 2
    def test_modification_equal_field_2(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test49.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test modify quotation before label 1
    def test_modify_quotation_before_l1(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test50.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test modify label 1
    def test_modify_l1(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test51.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test modify quote after label 1
    def test_modify_quotation_after_l1(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test52.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test modify quotation before value 1
    def test_modify_quotation_before_v1(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test53.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test modify IBAN country code
    def test_modify_country_code(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test54.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test modify IBAN numbers
    def test_modify_iban_num(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test55.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test modify quotation before label 2
    def test_modify_quotation_before_l2(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test56.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test modify quotation after value 1
    def test_modify_quotation_after_v1(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test57.json")
        result.assertThrows("The JSON does not have the expected structure")

    # Test modify AMOUNT
    def test_modify_AMOUNT(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test58.json")
        result.assertThrows("The JSON data does not have valid values")

    # Test modify quotation after label 2
    def test_modify_quote_after_l2(self):
        ob_invalid = AccountManager()
        result = ob_invalid.deposit_into_account("test59.json")
        result.assertThrows("The JSON does not have the expected structure")


if __name__ == '__main__':
    unittest.main()
