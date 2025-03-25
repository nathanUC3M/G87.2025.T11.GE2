"""Module """
import os
import re
from pathlib import Path
from datetime import datetime, timezone
import json
from .account_deposit import AccountDeposit
from .account_management_exception import AccountManagementException

class AccountManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_iban(iban: str):
        """
        Validates the IBAN, checks if the IBAN has the correct format and
        passes MOD-97 validation

        :param iban (str): The IBAN number to be validated
        :return: bool: True if the IBAN has the correct format and is valid, else false
        """
        # Valid IBAN: ES9121000418450200051332
        # Invalid IBAN: "ES91@1000418450200051332
        iban = iban.replace(" ", "").upper()
        iban_format = re.compile(r"^ES\d{2}[A-Z0-9]+$")

        # Below makes sure parameter matches the IBAN format
        if not iban_format.match(iban):
            return False
        # Moves the values at the indexes 0-3 to the back of the IBAN
        mixed_iban = iban[4:] + iban[:4]
        # Iterates over the IBAN changing the LETTERS to their numeric counterpart
        # according to the ASCII relation
        numeric_iban = "".join(str(ord(char) - 55) if char.isalpha()
                               else char for char in mixed_iban)

        # Converts the IBAN to an integer and performs the MOD 97 on it
        iban_int = int(numeric_iban)

        return iban_int % 97 == 1


    def validate_amount(self, amount: str):
        """
        Validates the amount to ensure it follows the correct format and is within valid limits.

        :param amount (str): The amount to be validated
        :return: bool: True if the amount is valid, otherwise False
        """
        # Check if the amount follows the correct format (must have two decimal places explicitly)
        amount = re.sub(r'[^\d.]', '', amount)
        if not re.match(r'^\d+\.\d{2}$', amount):
            return False

        try:
            # Convert to a float
            value = float(amount)
        except ValueError:
            return False

        # Check valid range
        return 10 <= value <= 1000

    def deposit_into_account(self, input_file: str) -> str:
        """
        Processes a deposit by reading account details from a JSON file,
        validating the IBAN and amount, and storing the deposit information.

        :param input_file (str): The name of the JSON file containing deposit details
        :return: str: A deposit signature confirming the transaction
        :raises AccountManagementException: If the file is missing, improperly formatted,
        contains invalid data, or encounters an internal error
        """
        # open file, verify account number and deposit value
        current_spot = os.getcwd()
        json_file_path = os.path.join(current_spot, 'json_files', input_file)
        try:
            # Initializes the path to check to make sure the file can be found
            path = Path(json_file_path)
            if not path.is_file():
                # Throws if the file is not found
                raise AccountManagementException("Data file not found")
            with open(json_file_path, "r", encoding="utf-8", newline="") as f:
                try:
                    data_list = json.load(f)
                except json.decoder.JSONDecodeError as e:
                    # Throws if the opened file is not in JSON format
                    raise AccountManagementException("File is not in JSON format") from e

                # Checks that the file includes IBAN, AMOUNT, and the given structure
                if not all(key in data_list for key in ["IBAN", "AMOUNT"]):
                    raise AccountManagementException("JSON does not have expected structure")

                # Takes away the IBAN and AMOUNT attached with the data values
                str_iban = data_list["IBAN"].strip()
                str_amount = data_list["AMOUNT"].strip()

                # Validates the given data values
                if not self.validate_iban(str_iban) or not self.validate_amount(str_amount):
                    raise AccountManagementException("The JSON data does not have valid values")

                ob_jam = AccountDeposit(str_iban, str_amount)

                # Places the deposits into an output folder
                output = "deposits.json"
                with open(output, "w", encoding="utf-8", newline="") as file:
                    json.dump(ob_jam.to_json(), file, indent=4)

                # Returns the signature of the deposit
                return ob_jam.deposit_signature
        except Exception as e:
            raise AccountManagementException(f"Internal processing error: {str(e)}") from e

    def calculate_balance(self, iban: str) -> bool:
        """
        Calculates the balance for a given IBAN by processing transactions from a JSON file,
        validating the IBAN and transaction amounts, and storing the calculated balance.

        :param iban (str): The IBAN for which to calculate the balance
        :return: bool: True if the balance calculation and storage were successful
        :raises AccountManagementException: If the IBAN is invalid,
        the transactions file is missing, improperly formatted, contains invalid data,
        or encounters an internal error during processing
        """
        current_spot = os.getcwd()
        json_file_path = os.path.join(current_spot, 'Transactions.json')

        try:
            if not self.validate_iban(iban):
                raise AccountManagementException("Invalid IBAN")

            try:
                with open(json_file_path, "r", encoding="utf-8") as file:
                    transactions = json.load(file)
            except FileNotFoundError as exc:
                raise AccountManagementException(f"Transactions file "
                                                 f"'{json_file_path}' not found") from exc
            except json.JSONDecodeError as exc:
                raise AccountManagementException(f"Invalid JSON format in "
                                                 f"'{json_file_path}'") from exc

            balance = 0.0
            iban_found = False
            for transaction in transactions:
                if transaction.get("IBAN") == iban:
                    iban_found = True
                    if ("amount" not in transaction or not
                    isinstance(transaction["amount"], (int, float, str))):
                        raise (AccountManagementException
                               (f"Invalid amount field in transaction: {transaction}"))
                    try:
                        amount = float(transaction["amount"])
                        balance += amount
                    except ValueError as exc:
                        raise AccountManagementException(
                            f"Invalid amount format in transaction: "
                            f"{transaction}") from exc

            if not iban_found:
                raise AccountManagementException(f"IBAN '{iban}' not found in transactions")

            # Save the balance data to the balance file
            balance_data = {
                "IBAN": iban,
                "balance": balance,
                "date": datetime.now(timezone.utc).timestamp()
            }
            current_spot_again = os.getcwd()
            json_file_path_new = os.path.join(current_spot_again, 'test_balances.json')
            try:
                with open(json_file_path_new, "a", encoding="utf-8") as file:
                    json.dump(balance_data, file)
                    file.write("\n")
            except Exception as e:
                raise AccountManagementException(f"Balance data saved incorrectly: "
                                                 f"{e}") from e

            return True
        except AccountManagementException as e:
            raise e
        except Exception as e:
            raise AccountManagementException(f"Error with processing: {e}") from e
