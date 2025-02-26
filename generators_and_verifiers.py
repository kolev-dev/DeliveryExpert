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
    for digit in range(10):
        current_random = random.randint(48, 57)
        generated_id += chr(current_random)

    return int(generated_id + "0000")