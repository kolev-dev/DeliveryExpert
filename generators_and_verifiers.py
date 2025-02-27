import random

#from files
# from user_info_manipulation import CURRENT_YEAR

# Each id should be stored in DB

class Generators:
    def generate_account_id(self):
        pass

    def generate_package_id(self):
        pass

    def generate_transaction_id(self):
        pass


def generate_account_id():
    """This method is used to identify users.
     The number ends with zeros, and its length is 16 characters.
     The first two characters represent the year the account was created"""

    generated_id = "25"
    #25 represents the current year: for example 2025 -> 25

    generated_id += str(random.randint(999_999_999, 1_000_000_000_0))
    # This code here generates random int with length of 10 characters

    return int(generated_id + "0000")