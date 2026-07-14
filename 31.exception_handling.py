"""
Exception handling in Python: catch and raise errors clearly for robustness.
Show built-in exceptions and custom exceptions with concise examples.
Demonstrate try/except/else/finally usage and clean-up patterns.
"""

import math


class MyException(
    Exception
):  # [Custom Exception] -> Output: defines a new exception type
    pass


class SecurityError(
    Exception
):  # [Security Exception] -> Output: may print message when raised
    def __init__(self, message):
        self.message = message
        print(message)  # [Side-effect] -> Output: prints security message

    def logout(self):
        print("logout")  # [Logout Action] -> Output: prints 'logout'


class Bank:  # [Bank Class] -> Output: provides withdraw() that may raise exceptions
    def __init__(self, balance):
        self.balance = balance

    def withdraw(
        self, amount
    ):  # [Validation] -> Output: raises MyException on invalid/insufficient funds
        if amount < 0:
            raise MyException("amount cannot be negative")
        if self.balance < amount:
            raise MyException("insufficient funds")
        self.balance = self.balance - amount


class Google:  # [Auth Class] -> Output: login() may raise SecurityError
    def __init__(self, name, email, password, device):
        self.name = name
        self.email = email
        self.password = password
        self.device = device

    def login(
        self, email, password, device
    ):  # raises SecurityError on unrecognized device
        if device != self.device:
            raise SecurityError("unrecognized device — security triggered")
        if email == self.email and password == self.password:
            print("welcome")  # [Auth Success] -> Output: prints 'welcome'
        else:
            print("login error")  # [Auth Fail] -> Output: prints 'login error'


def demonstrate_built_in_exceptions():  # [Built-ins] -> Output: demonstrates specific except blocks
    try:
        L = [1, 2, 3]
        _ = L[100]
    except IndexError as e:
        print(f"IndexError caught: {e}")  # [IndexError] -> Output: prints list index out of range

    try:
        d = {"name": "nitish"}
        _ = d["age"]
    except KeyError as e:
        print(f"KeyError caught: {e}")  # [KeyError] -> Output: prints missing key name

    try:
        _ = 1 + "a"
    except TypeError as e:
        print(f"TypeError caught: {e}")  # [TypeError] -> Output: prints unsupported operand types

    try:
        _ = int("a")
    except ValueError as e:
        print(f"ValueError caught: {e}")  # [ValueError] -> Output: prints invalid literal for int()

    try:
        print(k)
    except NameError as e:
        print(f"NameError caught: {e}")  # [NameError] -> Output: prints name 'k' is not defined

    try:
        L = [1, 2, 3]
        L.upper()
    except AttributeError as e:
        print(f"AttributeError caught: {e}")  # [AttributeError] -> Output: prints 'list' object has no attribute 'upper'


def demonstrate_try_except_else_finally():  # [Flow] -> Output: demonstrates try/except/else/finally behavior
    try:
        f = open("sample1.txt", "r")
    except FileNotFoundError:
        print("file not found" )  # [FileNotFoundError] -> Output: prints when file is missing
    except Exception:
        print("some other error occurred")  # [Other Error] -> Output: prints on unexpected errors
    else:
        print(f.read())  # [Else Block] -> Output: prints file contents when opened
        f.close()
    finally:
        print("this always executes")  # [Finally] -> Output: always runs


if __name__ == "__main__":
    with open("sample.txt", "w") as f:  # [Demo Setup] -> Output: creates sample.txt
        f.write("hello world")

    print("--- Built-in Exceptions ---")
    demonstrate_built_in_exceptions()  # [Run Demo] -> Output: prints built-in exception messages

    print("\n--- Try-Except-Else-Finally ---")
    demonstrate_try_except_else_finally()  # [Run Demo] -> Output: demonstrates control flow

    print("\n--- Bank Custom Exception ---")
    bank_obj = Bank(10000)
    try:
        bank_obj.withdraw(
            15000
        )  # [Withdraw Call] -> Output: raises MyException('insufficient funds')
    except MyException as e:
        print(e)  # [Handle MyException] -> Output: prints exception message
    else:
        print(bank_obj.balance)  # [On Success] -> Output: prints remaining balance

    print("\n--- Google Security Exception ---")
    google_obj = Google("nitish", "nitish@gmail.com", "1234", "android")
    try:
        google_obj.login(
            "nitish@gmail.com", "1234", "windows"
        )  # [Login Attempt] -> Output: mismatched device triggers SecurityError
    except SecurityError as e:
        e.logout()  # [Security Logout] -> Output: prints 'logout' after security message
    else:
        print(google_obj.name)  # [Successful Login] -> Output: prints user name
    finally:
        print("database connection closed")  # [Cleanup] -> Output: always prints
