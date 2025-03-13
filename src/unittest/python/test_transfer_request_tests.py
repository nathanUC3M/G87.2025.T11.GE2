"""class for testing the regsiter_order method"""
import unittest
import re
from uc3m_money import AccountManager

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    def test_something( self ):
        """dummy test"""
        self.assertEqual(True, False)
    def test_isyiung_tc1(self):
        am = AccountManager()
        res = am.is_young(17)
        self.assertEqual(True, res)

    def setUp(self):
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
        self.assertEqual(self.valid_request.transfer_type, "ORDINARY")
        self.assertEqual(self.valid_request.transfer_date, "04/02/2025")
        self.assertEqual(self.valid_request.transfer_amount, 400.34)

    # Test for valid and invalid IBANs
    def test_valid_iban(self):
        self.assertTrue(len(self.valid_request.from_iban) == 24)
        self.assertTrue(self.valid_request.from_iban.startswith('ES'))
        self.assertTrue(len(self.valid_request.to_iban) == 24)
        self.assertTrue(self.valid_request.to_iban.startswith('ES'))

    def test_invalid_iban_length(self):
        with self.assertRaises(ValueError):
            TransferRequest(
                from_iban="ES59",
                to_iban="ES6120809767496917112789",
                transfer_type="ORDINARY",
                transfer_concept="Payment for services",
                transfer_date="04/02/2025",
                transfer_amount=400.34
            )

    # Test for transfer type validations
    def test_invalid_transfer_type(self):
        with self.assertRaises(ValueError):
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
        with self.assertRaises(ValueError):
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
        transfer_code = self.valid_request.transfer_code
        self.assertEqual(len(transfer_code), 32)
        self.assertEqual(transfer_code, self.valid_request.transfer_code)


    def test_valid_concept_length(self):
        self.assertTrue(10 <= len(self.valid_request.transfer_concept) <= 30)

    def test_invalid_concept_length(self):
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

    def test_deposit_into_account(self):
        with self.assertTrue(self.valid_request.deposit_into_account):
            AccountManager.deposit_into_account("test.json")

if __name__ == '__main__':
    unittest.main()

