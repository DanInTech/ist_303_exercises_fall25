import datetime
import string
alphabet_lower = list(string.ascii_lowercase) #store alphabet in a list

def encode(input_text, shift):
    output_text = ''
    for character in input_text.lower():
        if character in alphabet_lower:
            #shifted position using module
            new_shift = 0
            new_shift = (ord(character) - ord('a') + shift) % 26
            output_text= output_text + (chr(ord('a') + new_shift))
        else:
            output_text += character
    return alphabet_lower, output_text

def decode(input_text, shift):
    output_text = ''
    for character in input_text.lower():
        if character in alphabet_lower:
            #shifted position using module
            new_shift = 0
            new_shift = (ord(character) - ord('a') - shift) % 26
            output_text= output_text + (chr(ord('a') + new_shift))
            # print(new_shift)
        else:
            output_text += character
    return output_text

class BankAccount:

    def __init__(self, name="Rainy", ID="1234", creation_date=datetime.date.today(), balance=0):
        self.name = name
        if isinstance(ID, (int, str)) and str(ID).isalnum:
            self.ID = str(ID)
        else:
            raise ValueError(f"String '{ID=}' is not alphanumeric")
        if creation_date <= datetime.date.today() and isinstance(creation_date, (datetime.datetime, datetime.date)):
            self.creation_date = creation_date
        else:
            raise ValueError(f"String '{creation_date=}' is not datetime or has a future date")
        if isinstance(balance, (int, float)):
            self.balance = balance
        else:
            raise ValueError(f"String '{balance=}' is not numeric")
        
    def deposit(self, amount):
        if amount < 0:
            # raise ValueError(f'{amount=} should be a positive number')
            print (f'{amount=} should be a positive number')
        else:
            self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def view_balance(self):
        return self.balance
    
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if datetime.date.today() - self.creation_date > datetime.timedelta(days=180):
            if self.balance - amount > 0:
                return super().withraw(amount)

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if super().withdraw(amount) < 0:
            self.balance -= 30