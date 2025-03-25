"""Module to test calculate balance method"""
import unittest
import json
import os
from src.main.python.uc3m_money.account_manager import AccountManager
from src.main.python.uc3m_money.account_management_exception import AccountManagementException


class TestCalculateBalanceWithProjectData(unittest.TestCase):
    """Class to test calculate balance method"""
    @classmethod
    def setUpClass(cls):
        """Backup original transactions file and create test manager"""
        cls.original_transactions = "Transactions.json"
        cls.test_balances = "test_balances.json"
        cls.manager = AccountManager()
        cls.manager.balance_file = cls.test_balances

    def tearDown(self):
        """Clean up balance file after each test"""
        try:
            os.remove(self.test_balances)
        except FileNotFoundError:
            pass

    def test_invalid_iban_format(self):
        """Test invalid IBAN (Path 1_2_3)"""
        with self.assertRaises(AccountManagementException):
            self.manager.calculate_balance("INVALID_IBAN_FORMAT")

    def test_valid_iban_with_transactions(self):
        """Test IBAN with multiple transactions (Path 1_2_4_5_6_7_8)"""
        # Test ES8658342044541216872704 which has 6 transactions
        result = self.manager.calculate_balance("ES8658342044541216872704")
        self.assertTrue(result)

        # Verify balance calculation (-1280.06 -3094.85 +2424.42 -1021.97 -4795.05 -2213.49)
        expected_balance = -1280.06 - 3094.85 + 2424.42 - 1021.97 - 4795.05 - 2213.49
        with open(self.test_balances, "r", encoding="utf-8") as f:
            last_entry = json.loads(f.readlines()[-1])
            self.assertAlmostEqual(last_entry["balance"], expected_balance, places=2)

    def test_valid_iban_not_in_file(self):
        """Test valid IBAN not found in transactions (Path 1_2_4_5_7_8)"""
        with self.assertRaises(AccountManagementException) as context:
            self.manager.calculate_balance("ES4900816334776271964371")
        self.assertIn("IBAN 'ES4900816334776271964371' not found in transactions",
                      str(context.exception))

    # EDGE CASE TESTS

    def test_iban_with_only_positive_transactions(self):
        """Test IBAN with only positive amounts (ES3559005439021242088295)"""
        result = self.manager.calculate_balance("ES3559005439021242088295")
        self.assertTrue(result)

        # Verify balance (+1258.75 +4028.28 +3981.26)
        expected_balance = 1258.75 + 4028.28 + 3981.26
        with open(self.test_balances, "r", encoding="utf-8") as f:
            last_entry = json.loads(f.readlines()[-1])
            self.assertAlmostEqual(last_entry["balance"], expected_balance, places=2)

    def test_iban_with_mixed_transactions(self):
        """Test IBAN with both positive and negative amounts (ES6211110783482828975098)"""
        result = self.manager.calculate_balance("ES6211110783482828975098")
        self.assertTrue(result)

        # Verify balance (-4470.37 +2265.68 +759.39 +1407.49 -3263.04 +4611.51 +4661.96)
        expected_balance = -4470.37 + 2265.68 + 759.39 + 1407.49 - 3263.04 + 4611.51 + 4661.96
        with open(self.test_balances, "r", encoding="utf-8") as f:
            last_entry = json.loads(f.readlines()[-1])
            self.assertAlmostEqual(last_entry["balance"], expected_balance, places=2)

    def test_iban_with_only_negative_transactions(self):
        """Test IBAN with only negative amounts (ES7156958200176924034556)"""
        result = self.manager.calculate_balance("ES7156958200176924034556")
        self.assertTrue(result)

        # Verify balance (-1643.06 -2768.05 -3805.22 -1118.72)
        expected_balance = -1643.06 - 2768.05 - 3805.22 - 1118.72
        with open(self.test_balances, "r", encoding="utf-8") as f:
            last_entry = json.loads(f.readlines()[-1])
            self.assertAlmostEqual(last_entry["balance"], expected_balance, places=2)


if __name__ == '__main__':
    unittest.main()
