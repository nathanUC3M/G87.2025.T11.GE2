"""Module """
import json

from src.main.python.uc3m_money import account_management_exception, TransferRequest, AccountDeposit


class AccountManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_iban(iban: str):
        """RETURNs TRUE IF THE IBAN RECEIVED IS VALID SPANISH IBAN,
        OR FALSE IN OTHER CASE"""
        return True

    def deposit_into_account(input_file):
        # open file, verify account number and deposit value
        try:
            with open(input_file, "r", encodings="utf-8", newline="") as f:
                data_list = json.load(input_file)

                strIBAN = data_list(1)
                strAMOUNT = data_list(2)
                hold = self.validate_iban(strIBAN)

                objAM = AccountDeposit(strAMOUNT, strIBAN)
        except FileNotFoundError:
            raise account_management_exception.AccountManagementException("File not found 444")
        except json.JSONDecodeError:
            raise account_management_exception.AccountManagementException("Invalid IBAN")
        return objAM.deposit_signature

    # objAM.deposit.into.account("test.json")
    # objAM is a fake object, we need to call it on account manager
    # check if previous files
