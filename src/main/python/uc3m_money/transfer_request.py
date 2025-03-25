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
                 to_iban: str,
                 transfer_concept: str,
                 transfer_date: str,
                 transfer_amount: float):
        # Validate all inputs during initialization
        if not AccountManager.validate_iban(from_iban):
            raise AccountManagementException("Invalid sender IBAN")
        if not AccountManager.validate_iban(to_iban):
            raise AccountManagementException("Invalid recipient IBAN")
        if transfer_type.upper() not in ["ORDINARY", "URGENT", "IMMEDIATE"]:
            raise AccountManagementException("Invalid transfer type")
        if not isinstance(transfer_concept, str):
            raise AccountManagementException("Concept must be a string")
        if not (10 <= len(transfer_concept) <= 30 and len(transfer_concept.split()) >= 2 and
                TransferRequest._validate_concept_words(transfer_concept)):
            raise AccountManagementException("Concept must be 10-30 chars with at least 2 words")
        if not TransferRequest.validate_date(transfer_date):
            raise AccountManagementException("Invalid transfer date")
        if not isinstance(transfer_amount, (int, float)):
            raise AccountManagementException("Amount must be a number")
        if not 10.00 <= float(transfer_amount) <= 10000.00:
            raise AccountManagementException("Amount must be between 10.00 and 10000.00")
        if isinstance(transfer_amount, float) and not round(transfer_amount, 2) == transfer_amount:
            raise AccountManagementException("Amount must have exactly 2 decimal places")

        self.__from_iban = from_iban
        self.__to_iban = to_iban
        self.__transfer_type = transfer_type.upper()
        self.__transfer_concept = transfer_concept  # Fixed attribute name
        self.__transfer_date = transfer_date
        self.__transfer_amount = float (transfer_amount)
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
            "transfer_concept": self.__transfer_concept,
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
                with open(filename, "r", encoding="utf-8") as file:
                    existing_transfers = [json.loads(line) for line in file if line.strip()]
            except FileNotFoundError:
                pass  # File doesn't exist yet (first transfer)

            # Check for duplicates (ignore timestamp/code)
            duplicate_keys = ["from_iban", "to_iban", "transfer_type",
                            "transfer_amount", "transfer_concept", "transfer_date"]
            for transfer in existing_transfers:
                if all(transfer[key] == transfer_data[key] for key in duplicate_keys):
                    raise AccountManagementException("Duplicate transfer detected")

            # Append new transfer
            with open(filename, "a", encoding="utf-8") as file:
                json.dump(transfer_data, file)
                file.write("\n")
        except AccountManagementException as e:
            raise e # Re-raise duplicate transfer exception directly
        except Exception as e:
            raise AccountManagementException(f"Failed to save transfer: "
                                             f"{str(e)}") from e

    def delete_from_json(self, filename: str = "transfers.json"):
        """Deletes transfer data from JSON file."""
        try:
            # Generate the data dictionary of this transfer using the same keys
            transfer_data = self.to_json()

            # Read existing transfers
            updated_transfers = []
            found = False
            try:
                with open(filename, "r", encoding="utf-8") as file:
                    existing_transfers = [json.loads(line) for line in file if line.strip()]

                    # Iterate over existing transfers to filter out the one to delete
                    for transfer in existing_transfers:
                        if all(transfer[key] == transfer_data[key] for key in transfer_data if
                               key != "time_stamp" and key != "transfer_code"):
                            found = True
                            continue
                        updated_transfers.append(transfer)

            except FileNotFoundError:
                raise AccountManagementException("File not found. No transfer to delete.")

            if not found:
                raise AccountManagementException("No matching transfer found to delete.")

            # Write the updated list back to the file, excluding the deleted transfer
            with open(filename, "w", encoding="utf-8") as file:
                for transfer in updated_transfers:
                    json.dump(transfer, file)
                    file.write("\n")

        except AccountManagementException as e:
            raise e  # Re-raise any custom exceptions
        except Exception as e:
            raise AccountManagementException(f"Failed to delete transfer: {str(e)}") from e

    @property
    def from_iban(self):
        """Sender's iban"""
        return self.__from_iban

    @from_iban.setter
    def from_iban(self, value):
        if not AccountManager.validate_iban(value):
            raise AccountManagementException("Invalid sender IBAN")
        self.__from_iban = value

    @property
    def to_iban(self):
        """receiver's iban"""
        return self.__to_iban

    @to_iban.setter
    def to_iban(self, value):
        if not AccountManager.validate_iban(value):
            raise AccountManagementException("Invalid recipient IBAN")
        self.__to_iban = value

    @property
    def transfer_type(self):
        """Property representing the type of transfer: ORDINARY, IMMEDIATE or URGENT"""
        return self.__transfer_type

    @transfer_type.setter
    def transfer_type(self, value):
        if value.upper() not in ["ORDINARY", "URGENT", "IMMEDIATE"]:
            raise AccountManagementException("Invalid transfer type")
        self.__transfer_type = value.upper()

    @property
    def transfer_amount(self):
        """Property representing the transfer amount"""
        return self.__transfer_amount

    @transfer_amount.setter
    def transfer_amount(self, value):
        if not isinstance(value, (int, float)):
            raise AccountManagementException("Amount must be a number")
        if not 10.00 <= float(value) <= 10000.00:
            raise AccountManagementException("Amount must be between 10.00 and 10000.00")
        if isinstance(value, float) and not round(value, 2) == value:
            raise AccountManagementException("Amount must have exactly 2 decimal places")
        self.__transfer_amount = float(value)
    @property
    def transfer_concept(self):
        """Property representing the transfer concept"""
        return self.__transfer_concept

    @transfer_concept.setter
    def transfer_concept(self, value):
        if not (10 <= len(value) <= 30 and len(value.split()) >= 2
                and TransferRequest._validate_concept_words(value)):
            raise AccountManagementException("Concept must be 10-30 chars letters with at "
                                             "least 2 words")
        self.__transfer_concept = value

    @property
    def transfer_date(self):
        """Property representing the transfer's date"""
        return self.__transfer_date

    @transfer_date.setter
    def transfer_date(self, value):
        if not TransferRequest.validate_date(value):
            raise AccountManagementException("Invalid transfer date")
        self.__transfer_date = value

    @property
    def time_stamp(self):
        """Read-only property that returns the timestamp of the request"""
        return self.__time_stamp

    @property
    def transfer_code(self):
        """Read-only property that returns the transfer code of the request"""
        return hashlib.md5(str(self).encode()).hexdigest()

    @staticmethod
    def _validate_concept_words(concept: str) -> bool:
        """Helper method to validate that all words contain only letters"""
        words = concept.split()
        return all(word.isalpha() for word in words)

    @staticmethod
    def validate_concept(concept: str) -> bool:
        """Returns bool regarding if the concept is in the given standards"""
        if not isinstance(concept, str):
            return False
        return (10 <= len(concept) <= 30 and len(concept.split()) >= 2
                and TransferRequest._validate_concept_words(concept))

    @staticmethod
    def validate_date(date: str) -> bool:
        """Returns bool regarding if the date is in the given standards"""
        try:
            # Attempt to parse the date using the expected format
            datetime.strptime(date, "%d/%m/%Y")
        except ValueError as exc:
            # Raise a custom exception on format error
            raise AccountManagementException("Invalid date format") from exc

            # If date format is correct, further validate the date values
        day, month, year = map(int, date.split("/"))
        if not 2025 <= year <= 2050:
            return False
        if not 1 <= month <= 12:
            return False
        if not 1 <= day <= 31:
            return False

        input_date = datetime.strptime(date, "%d/%m/%Y").replace(tzinfo=timezone.utc)
        current_date = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0,
                                                          microsecond=0)
        return input_date >= current_date

    @staticmethod
    def transfer_request(from_iban: str, to_iban: str, concept: str, transfer_type: str,
                         date: str, amount: float) -> str:
        """Static method to create and save a transfer request"""
        transfer = TransferRequest(
            from_iban=from_iban,
            to_iban=to_iban,
            transfer_type=transfer_type,
            transfer_concept=concept,
            transfer_date=date,
            transfer_amount=amount
        )
        transfer.save_to_json()
        return transfer.transfer_code
