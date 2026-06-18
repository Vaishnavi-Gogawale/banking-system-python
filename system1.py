"""
Banking System Mini Project
Features: OOP Concepts - Inheritance, Abstraction, Encapsulation, 
          Polymorphism, ClassMethod, StaticMethod
Author: Your Name
Date: 2026
"""

from abc import ABC, abstractmethod

class account:
    """Base class for all bank accounts"""
    bank_name = 'Bank Of India'   # class variable, common to all objects
    
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.__balance = balance  # private variable for encapsulation
    
    def deposit(self, amount):
        """Deposit money to account"""
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount > 0:
            self.__balance -= amount

    def get_balance(self):
        """Returns current balance"""
        return self.__balance

    @classmethod
    def get_bank_name(cls):
        """Returns bank name"""
        return cls.bank_name

    @staticmethod
    def bank_rules():
        """Display bank rules"""
        print("MAINTAIN MINIMUM BALANCE")
        print("BANK HOLIDAY ON SUNDAY ONLY")
    
    def __del__(self):
        print(f"Account of {self.holder_name} DELETED SUCCESSFULLY !!")

class intrest(ABC):
    """Abstract class for interest calculation"""
    @abstractmethod
    def intrest_rate(self):
        pass

class saving_account(account, intrest):
    """Saving Account: 5% interest, Min balance 1000"""
    def __init__(self, holder_name, balance):
        super().__init__(holder_name, balance)
    
    def intrest_rate(self):
        current_balance = self.get_balance()
        self.deposit(current_balance * 0.05)

    def withdraw(self, amount):
        if amount <= self.get_balance() - 1000:
            super().withdraw(amount)
        else:
            print("INSUFFICIENT FUNDS !! Minimum 1000 balance required")

class currentaccount(account, intrest):
    """Current Account: 1.5% interest, Overdraft 25000 allowed"""
    def __init__(self, holder_name, balance):
        super().__init__(holder_name, balance)
    
    def intrest_rate(self):
        current_balance = self.get_balance()
        if current_balance > 0:
            self.deposit(current_balance * 0.015)

    def withdraw(self, amount): 
        if amount <= self.get_balance() + 25000:
            super().withdraw(amount)
        else:
            print("INSUFFICIENT FUNDS !! Overdraft limit exceeded")

if __name__ == "__main__":
    print("Bank:", account.get_bank_name())
    account.bank_rules()
    print()
    
    # Saving Account Demo
    acc1 = saving_account("Vaishnavi Vikas Gogawale", 90000)
    acc1.deposit(20000)
    print(f"Savings BALANCE IS = {acc1.get_balance()}")
    acc1.intrest_rate()
    print(f"After Interest = {acc1.get_balance()}")
    acc1.withdraw(55000)
    print(f"BALANCE IS = {acc1.get_balance()}")
    
    print("\n" + "-"*40 + "\n")
    
    # Current Account Demo
    acc2 = currentaccount("ABC COP Ltd.", 5000)
    acc2.deposit(100000)
    print(f"Current BALANCE IS = {acc2.get_balance()}")
    acc2.intrest_rate()
    print(f"After Interest = {acc2.get_balance()}")
    acc2.withdraw(50000)
    print(f"BALANCE IS = {acc2.get_balance()}")