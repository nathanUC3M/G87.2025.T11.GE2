"""class for testing the regsiter_order method"""
import unittest
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
            from_iban="ES991234",
            to_iban="ES992345",
            transfer_type="ORDINARY",
            transfer_concept="Payment for services",
            transfer_date="04/02/2025",
            transfer_amount=400.34
        )

    def test_valid_transfer_request(self):
        self.assertEqual(self.valid_request.transfer_type, "ORDINARY")
        self.assertEqual(self.valid_request.transfer_date, "04/02/2025")
        self.assertEqual(self.valid_request.transfer_amount, 400.34)

    def test_invalid_transfer_type(self):
        with self.assertRaises(ValueError):
            TransferRequest(
                from_iban="ES991234",
                to_iban="ES992345",
                transfer_type="UNKNOWN",
                transfer_concept="Payment for services",
                transfer_date="04/02/2025",
                transfer_amount=400.34
            )

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            TransferRequest(
                from_iban="ES991234",
                to_iban="ES992345",
                transfer_type="ORDINARY",
                transfer_concept="Payment for services",
                transfer_date="2025-04-02",
                transfer_amount=400.34
            )

    def test_invalid_amount_range(self):
        with self.assertRaises(ValueError):
            TransferRequest(
                from_iban="ES991234",
                to_iban="ES992345",
                transfer_type="ORDINARY",
                transfer_concept="Payment for services",
                transfer_date="04/02/2025",
                transfer_amount=10000.01
            )
    def test_transfer_code(self):
        transfer_code = self.valid_request.transfer_code
        self.assertEqual(len(transfer_code), 32)
        self.assertEqual(transfer_code, self.valid_request.transfer_code)
if __name__ == '__main__':
    unittest.main()
