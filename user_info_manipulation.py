from generators_and_verifiers import generate_account_id
import re


class User:
    def __init__(self, full_name, phone_number, email, address):
        self.full_name = full_name
        self.phone_number = phone_number
        self.__email = email
        self.address = address

        self.user_account_id = generate_account_id()
        self.account_verified = False

    def print_id(self):
        return self.user_account_id

    def change(self, **kwargs):
        for key, value in kwargs.items():
            self.key = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        pattern = r'^[a-zA-Z0-9]+([._%+-]?[a-zA-Z0-9]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+$'
        if re.match(pattern, value) is object:
            self.__email = value
        raise ValueError()




a = User('hristo', '04909', 'lkfkjksfafdd', 'lkgl')
print(a.print_id())
