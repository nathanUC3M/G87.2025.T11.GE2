"""Module """
from account_management_exception import AccountManagementException
from datetime import datetime, timezone
import json
#sooooooo annnnnoying

class AccountManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_iban(iban: str):
        """RETURNs TRUE IF THE IBAN RECEIVED IS VALID SPANISH IBAN,
        OR FALSE IN OTHER CASE"""
        return iban.startswith("ES") and len(iban) == 24

    def calculate_balance(self, iban: str) -> bool:

        transactions_file = "Transactions.json"
        balance_file = "balances.json"

        try:
            if not self.validate_iban(iban):
                raise AccountManagementException("Invalid IBAN")

            try:
                with open(transactions_file, "r") as file:
                    transactions = json.load(file)
            except FileNotFoundError:
                raise AccountManagementException(f"Transactions file '{transactions_file}' not found")
            except json.JSONDecodeError:
                raise AccountManagementException(f"Invalid JSON format in '{transactions_file}'")

            balance = 0.0
            iban_found = False
            for transaction in transactions:
                if transaction.get("IBAN") == iban:
                    iban_found = True
                    str_amount = transaction.get("amount", "0")
                    try:
                        amount = float(str_amount)
                        balance += amount
                    except ValueError:
                        raise AccountManagementException(
                            f"Invalid amount format in transaction: {transaction}")

            if not iban_found:
                raise AccountManagementException(f"IBAN '{iban}' not found in transactions")

            # Save the balance data to the balance file
            balance_data = {
                "IBAN": iban,
                "balance": balance,
                "date": datetime.now(timezone.utc).timestamp()
            }
            try:
                with open(balance_file, "a") as file:
                    json.dump(balance_data, file)
                    file.write("\n")
            except Exception as e:
                raise AccountManagementException(f"Balance data saved incorrectly: {e}")

            return True
        except AccountManagementException as e:
            raise e
        except Exception as e:
            raise AccountManagementException(f"Error with processig: {e}")
