"""MODULE: transfer_request. Contains the transfer request class"""
import hashlib
import json
from datetime import datetime, timezone
from .account_management_exception import AccountManagementException
from .account_manager import AccountManager


class TransferRequest:
    """Class representing a transfer request"""
    def __init__(self,
                 from_iban: str,
                 transfer_type: str,
                 to_iban:str,
                 transfer_concept:str,
                 transfer_date:str,
                 transfer_amount:float):
        self.__from_iban = from_iban
        self.__to_iban = to_iban
        self.__transfer_type = transfer_type
        self.__concept = transfer_concept
        self.__transfer_date = transfer_date
        self.__transfer_amount = transfer_amount
        justnow = datetime.now(timezone.utc)
        self.__time_stamp = datetime.timestamp(justnow)

    def __str__(self):
        return "Transfer:" + json.dumps(self.__dict__)

    def to_json(self):
        """returns the object information in json format"""
        return {
            "from_iban": self.__from_iban,
            "to_iban": self.__to_iban,
            "transfer_type": self.__transfer_type,
            "transfer_amount": self.__transfer_amount,
            "transfer_concept": self.__concept,
            "transfer_date": self.__transfer_date,
            "time_stamp": self.__time_stamp,
            "transfer_code": self.transfer_code
        }

    def save_to_json(self, filename: str = "transfers.json"):
        """Saves transfer data to JSON file after checking for duplicates."""
        try:
            transfer_data = self.to_json()

            # Read existing transfers
            existing_transfers = []
            try:
                with open(filename, "r") as file:
                    for line in file:
                        if line.strip():
                            existing_transfers.append(json.loads(line))
            except FileNotFoundError:
                pass  # File doesn't exist yet (first transfer)

            # Check for duplicates (ignore timestamp/code)
            duplicate_keys = ["from_iban", "to_iban", "transfer_type",
                              "transfer_amount", "transfer_concept", "transfer_date"]
            for transfer in existing_transfers:
                if all(transfer[key] == transfer_data[key] for key in duplicate_keys):
                    raise AccountManagementException("Duplicate transfer detected")

            # Append new transfer
            with open(filename, "a") as file:
                json.dump(transfer_data, file)
                file.write("\n")
        except Exception as e:
            raise AccountManagementException(f"Failed to save transfer: {str(e)}")

    @property
    def from_iban(self):
        """Sender's iban"""
        return self.__from_iban

    @from_iban.setter
    def from_iban(self, value):
        self.__from_iban = value

    @property
    def to_iban(self):
        """receiver's iban"""
        return self.__to_iban

    @to_iban.setter
    def to_iban(self, value):
        self.__to_iban = value

    @property
    def transfer_type(self):
        """Property representing the type of transfer: REGULAR, INMEDIATE or URGENT """
        return self.__transfer_type
    @transfer_type.setter
    def transfer_type(self, value):
        self.__transfer_type = value

    @property
    def transfer_amount(self):
        """Property respresenting the transfer amount"""
        return self.__transfer_amount
    @transfer_amount.setter
    def transfer_amount(self, value):
        self.__transfer_amount = value

    @property
    def transfer_concept(self):
        """Property representing the transfer concept"""
        return self.__transfer_concept
    @transfer_concept.setter
    def transfer_concept(self, value):
        self.__transfer_concept = value

    @property
    def transfer_date( self ):
        """Property representing the transfer's date"""
        return self.__transfer_date
    @transfer_date.setter
    def transfer_date( self, value ):
        self.__transfer_date = value

    @property
    def time_stamp(self):
        """Read-only property that returns the timestamp of the request"""
        return self.__time_stamp

    @property
    def transfer_code(self):

        return hashlib.md5(str(self).encode()).hexdigest()

    @staticmethod
    def validate_concept(concept: str) -> bool:

        return 10 <= len(concept) <= 30 and len(concept.split()) >= 2

    @staticmethod
    def validate_date(date: str) -> bool:

        try:
            day, month, year = map(int, date.split("/"))
            if not (2025 <= year <= 2050):
                return False
            if not (1 <= month <= 12):
                return False
            if not (1 <= day <= 31):
                return False

            input_date = datetime.strptime(date, "%d/%m/%Y").replace(tzinfo=timezone.utc)
            current_date = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0,
                                                              microsecond=0)

            if input_date < current_date:
                return False

            return True
        except ValueError:
            return False
    @staticmethod
    def transfer_request(from_iban: str, to_iban: str, concept: str, type: str, date: str,
                         amount: float) -> str:
        """
        Processes a transfer request and returns a transfer code (MD5 hash).

        Arguments:
            from_iban (str): The IBAN of the sender's account.
            to_iban (str): The IBAN of the receiver's account.
            concept (str): A description of the transfer (10-30 characters, at least two words).
            type (str): The type of transfer (ORDINARY, URGENT, or IMMEDIATE).
            date (str): The date of the transfer in "DD/MM/YYYY" format.
            amount (float): The amount to transfer (10.00 <= amount <= 10000.00).

        Returns:
            str: The transfer code (MD5 hash) representing the transfer.

        Raises:
            AccountManagementException: If any input is invalid or the transfer cannot be processed.
        """
        try:
            # Validate inputs before creating the TransferRequest object
            if (not AccountManager.validate_iban(from_iban) or not AccountManager.validate_iban(to_iban)):
                raise AccountManagementException("Invalid IBAN")
            if not TransferRequest.validate_concept(concept):
                raise AccountManagementException("Invalid concept")
            if type not in ["ORDINARY", "URGENT", "IMMEDIATE"]:
                raise AccountManagementException("Invalid transfer type")
            if not TransferRequest.validate_date(date):
                raise AccountManagementException("Invalid date")
            if not (10.00 <= amount <= 10000.00):
                raise AccountManagementException("Invalid amount")

            if isinstance(amount, float):
                if not round(amount, 2) == amount:
                    raise AccountManagementException("Amount must have ≤2 decimal places")
                from_iban=from_iban,

            # TransferRequest object
            transfer = TransferRequest(
                from_iban=from_iban,
                to_iban=to_iban,
                transfer_type=type,
                transfer_concept=concept,
                transfer_date=date,
                transfer_amount=amount
            )

            transfer.save_to_json()
            return transfer.transfer_code

        except Exception as e:
            raise AccountManagementException(str(e))
