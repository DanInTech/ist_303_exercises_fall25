## Pair Programming Exercise #3

### Daniel Perez
### David Merten-Jones

import string

def encode(input_text, shift=0):
    #store ascii lowercase alphabet in list
    alpha_lc = list(string.ascii_lowercase)
    #dictionary converts lowercase to index number
    lc_to_num = {letter:alpha_lc.index(letter) for letter in alpha_lc}
    #dictionary converts index number to lowercase
    num_to_lc = {value:key for key, value in lc_to_num.items()}
    
    #If shift is negative, make it positive
    while shift < 0:
        shift += 26

    #initialize output
    output_text = ''

    #append characters to output, shifting if they are letters
    #change upppercase to lowercase
    for char in input_text.lower():
        if char in alpha_lc:
            output_text += num_to_lc[(lc_to_num[char]+shift)%26]
        else:
            output_text += char

    #return output text
    return alpha_lc, output_text

def decode(input_text, shift=0):
    #store ascii lowercase alphabet in list
    alpha_lc = list(string.ascii_lowercase)
    #dictionary converts lowercase to index number
    lc_to_num = {letter:alpha_lc.index(letter) for letter in alpha_lc}
    #dictionary converts index number to lowercase
    num_to_lc = {value:key for key, value in lc_to_num.items()}
    
    #If shift is negative, make it positive
    while shift < 0:
        shift += 26

    #initialize output
    output_text = ''

    #append characters to output, shifting if they are letters
    #change upppercase to lowercase
    for char in input_text.lower():
        if char in alpha_lc:
            output_text += num_to_lc[(26 + lc_to_num[char] - shift) % 26]
        else:
            output_text += char

    #return output text
    return output_text
    
import datetime

class BankAccount:
    def __init__(self, name='Rainy', id_num='1234', creation_date=datetime.date.today(), balance=0):
        self.name = name
        self.id_num = id_num
        self.creation_date = creation_date
        self.balance = balance
        if self.creation_date > datetime.date.today():
            raise Exception

    def deposit(self, amount):

        if amount >= 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
            

    def view_balance():
        pass

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.creation_date <= datetime.date.today() - datetime.timedelta(days=180):
            if self.balance >= amount:
                self.balance -= amount
        return self.balance

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 30
        return self.balance
    
