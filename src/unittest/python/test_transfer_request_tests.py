"""class for testing the register_order method"""
import json
import os
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
            transfer_date="02/04/2025",
            transfer_amount=400.34
        )

    # Test for valid transfer requests
    def test_valid_transfer_request(self):
        """Test that a valid transfer request is correctly initialized."""
        self.assertEqual(self.valid_request.transfer_type, "ORDINARY")
        self.assertEqual(self.valid_request.transfer_date, "02/04/2025")
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
                transfer_date="02/04/2025",
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
                transfer_date="02/04/2025",
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
                transfer_date="02/04/2025",
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
            to_iban="ES9514659166625939748647",
            transfer_type="ORDINARY",
            transfer_concept="Payment for services",
            transfer_date="02/04/2025",
            transfer_amount=400.34
        )
        request.save_to_json()  # First save should succeed
        with self.assertRaises(AccountManagementException):
            request.save_to_json()  # Second save should fail
        request.delete_from_json()
    def test_invalid_decimal_places(self):
        """Test that an amount with too many decimal places raises an exception."""
        with self.assertRaises(AccountManagementException):
            TransferRequest(
                from_iban="ES3300813648834254477713",
                to_iban="ES6730044874916517558463",
                transfer_type="ORDINARY",
                transfer_concept="Payment for services",
                transfer_date="04/02/2025",
                transfer_amount=400.345  # 3 decimal places
            )

    def test_invalid_from_iban_non_string(self):
        """Test that a non-string from_iban raises an exception (ECNV1)."""
        with self.assertRaises(AccountManagementException):
            TransferRequest(
                from_iban=123456789,  # Integer (invalid type)
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept="Payment for services",
                transfer_date="02/04/2025",
                transfer_amount=400.34
            )

    def test_invalid_concept_non_string(self):
        """ECNV7: Non-string concept"""
        with self.assertRaises(AccountManagementException):
            TransferRequest(
                from_iban="ES3300813648834254477713",
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept=12345,
                transfer_date="02/04/2025",
                transfer_amount=400.34
            )
    def test_invalid_no_space_concept(self):
        """ECNV9: Two words but no space"""
        with self.assertRaises(AccountManagementException):
            TransferRequest(
                from_iban="ES3300813648834254477713",
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept="Payment-services",  # Hyphen instead of space
                transfer_date="02/04/2025",
                transfer_amount=400.34
            )

    def test_invalid_special_chars_concept(self):
        """ECNV10: Contains non-letter characters"""
        invalid_concepts = [
            "Payment @services",  # Special char
            "Invoice #123",  # Special char
            "Fee! payment",  # Special char
        ]
        for concept in invalid_concepts:
            with self.subTest(concept=concept):
                with self.assertRaises(AccountManagementException):
                    TransferRequest(
                        from_iban="ES3300813648834254477713",
                        to_iban="ES6120809767496917112789",
                        transfer_type="ORDINARY",
                        transfer_concept=concept,
                        transfer_date="02/04/2025",
                        transfer_amount=400.34
                    )

    def test_invalid_long_concept(self):
        """ECNV12: Concept > 30 chars"""
        with self.assertRaises(AccountManagementException):
            TransferRequest(
                from_iban="ES3300813648834254477713",
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept="A" * 15 + " " + "B" * 16,  # 31 chars
                transfer_date="02/04/2025",
                transfer_amount=400.34
            )

    def test_boundary_length_concepts(self):
        """Boundary values for length (10 and 30 chars)"""
        # Lower boundary (10 chars)
        try:
            TransferRequest(
                from_iban="ES3300813648834254477713",
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept="A" * 5 + " " + "B" * 5,  # 10 chars
                transfer_date="02/04/2025",
                transfer_amount=400.34
            )
        except AccountManagementException:
            self.fail("10-character concept failed")

        # Upper boundary (30 chars)
        try:
            TransferRequest(
                from_iban="ES3300813648834254477713",
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept="A" * 14 + " " + "B" * 15,  # 30 chars
                transfer_date="02/04/2025",
                transfer_amount=400.34
            )
        except AccountManagementException:
            self.fail("30-character concept failed")


    def test_non_float_amount(self):
        """Tests the inability to accept non float amounts"""
        invalid_amounts = [
            "100.00",  # String
            100,  # Integer
            None,  # None
            ["100.00"]  # List
        ]
        for amount in invalid_amounts:
            with self.subTest(amount=amount):
                with self.assertRaises(AccountManagementException):
                    TransferRequest(
                        from_iban="ES5930045568068979213666",
                        to_iban="ES6120809767496917112789",
                        transfer_type="ORDINARY",
                        transfer_concept="Payment for services",
                        transfer_date="04/02/2025",
                        transfer_amount=amount
                    )
    def test_transfer_code_not_string(self):
        """ECNV20: Verify transfer code can't be non-string"""
        # This case is theoretically impossible since MD5 always returns string
        transfer = TransferRequest( from_iban="ES5930045568068979213666",
            to_iban="ES6120809767496917112789",
            transfer_type="ORDINARY",
            transfer_concept="Payment for services",
            transfer_date="02/04/2025",
            transfer_amount=400.34)
        self.assertIsInstance(transfer.transfer_code, str)
    def test_transfer_code_not_md5(self):
        """ECNV21: Verify transfer code is always MD5"""
        # This case is theoretically impossible with current implementation
        transfer = TransferRequest( from_iban="ES5930045568068979213666",
            to_iban="ES6120809767496917112789",
            transfer_type="ORDINARY",
            transfer_concept="Payment for services",
            transfer_date="02/04/2025",
            transfer_amount=400.34)
        code = transfer.transfer_code
        self.assertEqual(len(code), 32)
        self.assertTrue(all(c in '0123456789abcdef' for c in code))

    def test_valid_file_output(self):
        """ECV19: Verify transfer saves correctly to file"""
        test_file = "test_transfers.json"

        # Clean up if file exists
        if os.path.exists(test_file):
            os.remove(test_file)

        transfer = TransferRequest(
            from_iban="ES9121000418450200051332",
            to_iban="ES1920802632317171556954",
            transfer_type="ORDINARY",
            transfer_concept="Payment for services",
            transfer_date="02/04/2025",
            transfer_amount=400.34
        )

        # First save should succeed
        transfer.save_to_json(test_file)

        # Verify file exists and contains the transfer
        self.assertTrue(os.path.exists(test_file))

        # Read the file line by line (since it contains one JSON object per line)
        with open(test_file, 'r', encoding= 'utf-8') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 1)  # Should be exactly one line

            # Parse the first line as JSON
            data = json.loads(lines[0])
            self.assertEqual(data['from_iban'], "ES9121000418450200051332")

        # Clean up
        transfer.delete_from_json(test_file)

    def test_corrupted_file_output(self):
        """ECNV22: Handle corrupted file content"""
        # Create corrupted file
        with open("test_transfers.json", 'w', encoding= 'utf-8') as f:
            f.write("not valid json")

        transfer = TransferRequest(from_iban="ES9121000418450200051332",
            to_iban="ES1920802632317171556954",
            transfer_type="ORDINARY",
            transfer_concept="Payment for services",
            transfer_date="02/04/2025",
            transfer_amount=400.34)
        with self.assertRaises(AccountManagementException):
            transfer.save_to_json("test_transfers.json")

    def test_invalid_account_numbers(self):
        """ECNV23: Verify invalid IBANs raise exceptions"""
        invalid_cases = [
            {'from_iban': 'ES91', 'to_iban': 'ES7620770024003102575766'},  # Short from
            {'from_iban': 'ES9121000418450200051332', 'to_iban': 'ES76'},  # Short to
            {'from_iban': 'XX9121000418450200051332', 'to_iban': 'ES7620770024003102575766'},
            # Wrong country
            {'from_iban': 'ES9121000418450200051332', 'to_iban': 'XX7620770024003102575766'}
            # Wrong country
        ]

        valid_params = {
            'from_iban': 'ES9121000418450200051332',
            'to_iban': 'ES7620770024003102575766',
            'transfer_type': 'ORDINARY',
            'transfer_concept': 'Valid concept text',
            'transfer_date': "02/04/2025",
            'transfer_amount': 100.00
        }

        for case in invalid_cases:
            with self.subTest(case=case):
                params = valid_params.copy()
                params.update(case)
                with self.assertRaises(AccountManagementException):
                    TransferRequest(**params)



    def test_invalid_quantity(self):
        """ECNV27: Verify invalid amounts raise exceptions"""
        invalid_amounts = [
            9.99,  # Below minimum
            10000.01,  # Above maximum
            100.001,  # Too many decimals
            '100.00',  # Wrong type
            None  # Wrong type
        ]

        valid_params = {
            'from_iban': 'ES9121000418450200051332',
            'to_iban': 'ES7620770024003102575766',
            'transfer_type': 'ORDINARY',
            'transfer_concept': 'Valid concept text',
            'transfer_date': "02/04/2025",
            'transfer_amount': 100.00
        }

        for amount in invalid_amounts:
            with self.subTest(amount=amount):
                params = valid_params.copy()
                params['transfer_amount'] = amount
                with self.assertRaises(AccountManagementException):
                    TransferRequest(**params)

    def test_invalid_format_requirements(self):
        """ECNV29: Verify invalid formats raise exceptions"""
        invalid_cases = [
            {'from_iban': 'ES91', 'transfer_concept': 'Valid', 'transfer_amount': 100.00},
            # Multiple issues
            {'transfer_type': 'INVALID', 'transfer_date': '32/01/2025'},  # Multiple issues
            {'transfer_concept': 'A', 'transfer_amount': 9.99}  # Multiple issues
        ]

        valid_params = {
            'from_iban': 'ES9121000418450200051332',
            'to_iban': 'ES7620770024003102575766',
            'transfer_type': 'ORDINARY',
            'transfer_concept': 'Valid concept text',
            'transfer_date': "02/04/2025",
            'transfer_amount': 100.00
        }

        for case in invalid_cases:
            with self.subTest(case=case):
                params = valid_params.copy()
                params.update(case)
                with self.assertRaises(AccountManagementException):
                    TransferRequest(**params)

if __name__ == '__main__':
    unittest.main()
