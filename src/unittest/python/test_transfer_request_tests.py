"""class for testing the register_order method"""
import unittest
from src.main.python.uc3m_money.transfer_request import TransferRequest
from src.main.python.uc3m_money.account_management_exception import AccountManagementException

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    def setUp(self):
        """Set up a valid transfer request for use in test cases."""
        self.valid_request = TransferRequest(
            from_iban="ES5930045568068979213666",
            to_iban="ES6120809767496917112789",
            transfer_type="ORDINARY",
            transfer_concept="Payment for services",
            transfer_date="04/02/2025",
            transfer_amount=400.34
        )

    # Test for valid transfer requests
    def test_valid_transfer_request(self):
        """Test that a valid transfer request is correctly initialized."""
        self.assertEqual(self.valid_request.transfer_type, "ORDINARY")
        self.assertEqual(self.valid_request.transfer_date, "04/02/2025")
        self.assertEqual(self.valid_request.transfer_amount, 400.34)

    # Test for valid and invalid IBANs
    def test_valid_iban(self):
        """Test that the IBANs are valid in format and length."""
        self.assertTrue(len(self.valid_request.from_iban) == 24)
        self.assertTrue(self.valid_request.from_iban.startswith('ES'))
        self.assertTrue(len(self.valid_request.to_iban) == 24)
        self.assertTrue(self.valid_request.to_iban.startswith('ES'))

    def test_invalid_from_iban_length(self):
        """Test that an IBAN with an invalid length raises a ValueError."""
        with self.assertRaises(AccountManagementException):
            TransferRequest(
                from_iban="ES59",
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept="Payment for services",
                transfer_date="04/02/2025",
                transfer_amount=400.34
            )

    def test_invalid_to_iban_length(self):
        """Test that an IBAN with an invalid length raises a ValueError."""
        with self.assertRaises(AccountManagementException):
            TransferRequest(
                from_iban="ES6120809767496917112789",
                to_iban="ES59",
                transfer_type="ORDINARY",
                transfer_concept="Payment for services",
                transfer_date="04/02/2025",
                transfer_amount=400.34
            )

    # Test for transfer type validations
    def test_invalid_transfer_type(self):
        """Test that an invalid transfer type raises a ValueError."""
        with self.assertRaises(AccountManagementException):
            TransferRequest(
                from_iban="ES5930045568068979213666",
                to_iban="ES6120809767496917112789",
                transfer_type="UNKNOWN",
                transfer_concept="Payment for services",
                transfer_date="04/02/2025",
                transfer_amount=400.34
            )

    # Test for date validations
    def test_invalid_date_format(self):
        """Test that an invalid date format raises a ValueError."""
        with self.assertRaises(AccountManagementException):
            TransferRequest(
                from_iban="ES5930045568068979213666",
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept="Payment for services",
                transfer_date="2025-04-02",
                transfer_amount=400.34
            )

    # Test for amount validations
    def test_invalid_amount_range(self):
        """Test that an amount out of the valid range raises a ValueError."""
        with self.assertRaises(AccountManagementException):
            TransferRequest(
                from_iban="ES5930045568068979213666",
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept="Payment for services",
                transfer_date="04/02/2025",
                transfer_amount=10000.01
            )

    def test_transfer_code(self):
        """Test that the transfer code is generated correctly."""
        transfer_code = self.valid_request.transfer_code
        self.assertEqual(len(transfer_code), 32)
        self.assertEqual(transfer_code, self.valid_request.transfer_code)


    def test_valid_concept_length(self):
        """Test that the transfer concept length is within the valid range."""
        self.assertTrue(10 <= len(self.valid_request.transfer_concept) <= 30)

    def test_invalid_concept_length(self):
        """Test that an invalid transfer concept length raises a ValueError."""
        with self.assertRaises(AccountManagementException):
            TransferRequest(
                from_iban="ES5930045568068979213666",
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept="Short",
                transfer_date="04/02/2025",
                transfer_amount=400.34
            )

    def test_boundary_date_values(self):
        """Test that boundary date values are correctly validated."""
        with self.assertRaises(AccountManagementException):
            TransferRequest(from_iban="ES5930045568068979213666",
                            to_iban="ES6120809767496917112789",
                            transfer_type="ORDINARY", transfer_concept="Payment for services",
                            transfer_date="00/02/2025", transfer_amount=400.34)  # BVNV9
        with self.assertRaises(AccountManagementException):
            TransferRequest(from_iban="ES5930045568068979213666",
                            to_iban="ES6120809767496917112789",
                            transfer_type="ORDINARY", transfer_concept="Payment for services",
                            transfer_date="32/01/2025", transfer_amount=400.34)  # BVNV10

    def test_boundary_amount_values(self):
        """Test that boundary values for amount are correctly validated."""
        with self.assertRaises(AccountManagementException):
            TransferRequest(from_iban="ES5930045568068979213666",
                            to_iban="ES6120809767496917112789",
                            transfer_type="ORDINARY", transfer_concept="Payment for services",
                            transfer_date="04/02/2025", transfer_amount=9.99)  # BVNV13
        with self.assertRaises(AccountManagementException):
            TransferRequest(from_iban="ES5930045568068979213666",
                            to_iban="ES6120809767496917112789",
                            transfer_type="ORDINARY", transfer_concept="Payment for services",
                            transfer_date="04/02/2025", transfer_amount=10000.01)  # BVNV14

    def test_past_date(self):
        """Test that a past transfer date raises an AccountManagementException."""
        with self.assertRaises(AccountManagementException):
            TransferRequest(
                from_iban="ES5930045568068979213666",
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept="Payment for services",
                transfer_date="01/01/2020",
                transfer_amount=400.34
            )

    def test_duplicate_transfer(self):
        """Test that saving the same transfer twice raises an exception."""
        # Use the same data as setUp for consistency
        request = TransferRequest(
            from_iban="ES5930045568068979213666",
            to_iban="ES6120809767496917112789",
            transfer_type="ORDINARY",
            transfer_concept="Payment for services",
            transfer_date="04/02/2025",
            transfer_amount=400.34
        )
        request.save_to_json()  # First save should succeed
        with self.assertRaises(AccountManagementException):
            request.save_to_json()  # Second save should fail

    def test_invalid_decimal_places(self):
        """Test that an amount with too many decimal places raises an exception."""
        with self.assertRaises(AccountManagementException):
            TransferRequest(
                from_iban="ES5930045568068979213666",
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept="Payment for services",
                transfer_date="04/02/2025",
                transfer_amount=400.345  # 3 decimal places
            )

if __name__ == '__main__':
    unittest.main()
