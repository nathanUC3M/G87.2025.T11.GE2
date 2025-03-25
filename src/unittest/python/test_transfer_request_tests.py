"""Class for testing the register_order method"""
import unittest
from src.main.python.uc3m_money import AccountManager, TransferRequest

class MyTestCase(unittest.TestCase):
    """Class for testing the register_order method"""
    def test_isyoung_tc1(self):
        """Tests if the is_young method correctly identifies a 17-year-old as young."""
        am = AccountManager()
        res = am.is_young(17)
        self.assertEqual(True, res)

    def setUp(self):
        """Sets up a valid TransferRequest instance for use in multiple test cases."""
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
        """Tests if the valid TransferRequest has the correct attributes."""
        self.assertEqual(self.valid_request.transfer_type, "ORDINARY")
        self.assertEqual(self.valid_request.transfer_date, "04/02/2025")
        self.assertEqual(self.valid_request.transfer_amount, 400.34)

    # Test for valid and invalid IBANs
    def test_valid_iban(self):
        """Tests if the IBANs in the transfer request have the correct format."""
        self.assertTrue(len(self.valid_request.from_iban) == 24)
        self.assertTrue(self.valid_request.from_iban.startswith('ES'))
        self.assertTrue(len(self.valid_request.to_iban) == 24)
        self.assertTrue(self.valid_request.to_iban.startswith('ES'))

    def test_invalid_iban_length(self):
        """Tests if an invalid IBAN length raises a ValueError."""
        with self.assertRaises(ValueError):
            TransferRequest(
                from_iban="ES59",
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept="Payment for services",
                transfer_date="04/02/2025",
                transfer_amount=400.34
            )

    def test_invalid_transfer_type(self):
        """Tests if an invalid transfer type raises a ValueError."""
        with self.assertRaises(ValueError):
            TransferRequest(
                from_iban="ES5930045568068979213666",
                to_iban="ES6120809767496917112789",
                transfer_type="UNKNOWN",
                transfer_concept="Payment for services",
                transfer_date="04/02/2025",
                transfer_amount=400.34
            )

    def test_invalid_date_format(self):
        """Tests if an incorrectly formatted date raises a ValueError."""
        with self.assertRaises(ValueError):
            TransferRequest(
                from_iban="ES5930045568068979213666",
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept="Payment for services",
                transfer_date="2025-04-02",
                transfer_amount=400.34
            )

    def test_invalid_amount_range(self):
        """Tests if a transfer amount beyond the valid range raises a ValueError."""
        with self.assertRaises(ValueError):
            TransferRequest(
                from_iban="ES5930045568068979213666",
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept="Payment for services",
                transfer_date="04/02/2025",
                transfer_amount=10000.01
            )


    def test_transfer_code(self):
        """Tests if the transfer_code is correctly
        generated and has a length of 32 characters."""
        transfer_code = self.valid_request.transfer_code
        self.assertEqual(len(transfer_code), 32)
        self.assertEqual(transfer_code, self.valid_request.transfer_code)


    def test_valid_concept_length(self):
        """Tests if the transfer concept length is within the allowed range."""
        self.assertTrue(10 <= len(self.valid_request.transfer_concept) <= 30)

    def test_invalid_concept_length(self):
        """Tests if a too-short transfer concept raises a ValueError."""
        with self.assertRaises(ValueError):
            TransferRequest(
                from_iban="ES5930045568068979213666",
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept="Short",
                transfer_date="04/02/2025",
                transfer_amount=400.34
            )

    def test_boundary_date_values(self):
        """Tests if boundary values for the date field raise a ValueError."""
        with self.assertRaises(ValueError):
            TransferRequest(from_iban="ES5930045568068979213666",
                            to_iban="ES6120809767496917112789",
                            transfer_type="ORDINARY", transfer_concept="Payment for services",
                            transfer_date="00/02/2025", transfer_amount=400.34)  # BVNV9
        with self.assertRaises(ValueError):
            TransferRequest(from_iban="ES5930045568068979213666",
                            to_iban="ES6120809767496917112789",
                            transfer_type="ORDINARY", transfer_concept="Payment for services",
                            transfer_date="32/01/2025", transfer_amount=400.34)  # BVNV10

    def test_boundary_amount_values(self):
        """Tests if transfer amounts below or above valid limits raise a ValueError."""
        with self.assertRaises(ValueError):
            TransferRequest(from_iban="ES5930045568068979213666",
                            to_iban="ES6120809767496917112789",
                            transfer_type="ORDINARY", transfer_concept="Payment for services",
                            transfer_date="04/02/2025", transfer_amount=9.99)  # BVNV13
        with self.assertRaises(ValueError):
            TransferRequest(from_iban="ES5930045568068979213666",
                            to_iban="ES6120809767496917112789",
                            transfer_type="ORDINARY", transfer_concept="Payment for services",
                            transfer_date="04/02/2025", transfer_amount=10000.01)  # BVNV14

if __name__ == '__main__':
    unittest.main()
