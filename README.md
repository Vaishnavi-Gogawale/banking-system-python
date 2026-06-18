# 🏦 Banking System - Python OOP Mini Project

A simple banking system built using Python to demonstrate Object-Oriented Programming concepts. This is a college mini-project.

✨ Features
- Encapsulation: Private balance variable `__balance` with getter/setter methods
- Inheritance: `saving_account` and `currentaccount` inherit from `account` class
- Abstraction: Abstract class `intrest` with abstract method `intrest_rate()`
- Polymorphism: Different `withdraw()` and `intrest_rate()` implementations for each account type
- Class Method: `get_bank_name()` common for all accounts
- Static Method: `bank_rules()` independent of class instance

📋 Account Types
| Account Type | Interest Rate | Special Rule |
| --- | --- | --- |
| Savings Account | 5% | Minimum balance: ₹1000 |
| Current Account | 1.5% | Overdraft up to ₹25,000 |

🚀 How to Run
1. Download `system1.py`
2. Run the file in terminal:
   ```bash
   python system1.py
