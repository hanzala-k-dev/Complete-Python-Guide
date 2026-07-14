"""
This file demonstrates core OOP concepts in Python with practical examples.
Each section includes inline comments and expected outputs for learner clarity.
"""


# Simple class with class attributes and an instance method
class Car:
    color = "blue"  # class attribute shared by all instances
    model = "sports"  # class attribute

    def calculate_avg_speed(self, km, time):
        # average speed = distance / time
        return km / time


# Create an instance of Car (object)
wagonr = Car()
# wagonr is a Car instance; no output here


# DUNDER METHODS and operator overloading via a Fraction class
class Fraction:
    def __init__(self, n, d):
        # store numerator and denominator as instance attributes
        self.num = n
        self.den = d

    def __str__(self):
        # string representation for printing
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        # implement fraction addition
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)

    def __sub__(self, other):
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)

    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)

    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return Fraction(temp_num, temp_den)


x = Fraction(4, 5)
y = Fraction(5, 6)
print(x + y)  # expected output: 49/30


# Demonstrating 'self' and object mutation via references
class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


def greet(customer_obj):
    # Uses the passed object reference; can mutate object attributes
    if customer_obj.gender == "Male":
        print(f"Hello {customer_obj.name} sir")
    else:
        print(f"Hello {customer_obj.name} ma'am")

    # Mutate the original object to show reference semantics
    customer_obj.name = "Rauf"


cust = Customer("Hanzala", "Male")
greet(cust)  # prints: Hello Hanzala sir
print(cust.name)  # prints: Rauf (name was mutated inside greet)


# DATA ENCAPSULATION & ACCESS CONTROL using name mangling
class Atm:
    def __init__(self):
        self.__pin = ""  # pseudo-private attribute (name-mangled)
        self.__balance = 0  # pseudo-private attribute

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        # enforce type-checking when setting the PIN
        if isinstance(new_pin, str):
            self.__pin = new_pin
            print("Pin changed successfully")
        else:
            print("Not allowed: PIN must be a string")


# STATIC VARIABLES AND METHODS example
class PremiumAtm:
    __counter = 1  # private class-level counter

    def __init__(self):
        self.sno = PremiumAtm.__counter
        PremiumAtm.__counter += 1

    @staticmethod
    def get_counter():
        return PremiumAtm.__counter


# AGGREGATION & INHERITANCE
class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state


class User:
    def __init__(self, name, gender, address_obj):
        self.name = name
        self.gender = gender
        self.address = address_obj  # aggregation: User has an Address

    def login(self):
        print("Login completed")


class Student(User):
    # Student inherits User behavior and adds enroll()
    def enroll(self):
        print("Enrolled in course")


# SUPER() keyword and constructor delegation
class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera


class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram


# POLYMORPHISM: method overriding example
class PhoneAction:
    def buy(self):
        print("Buying a generic phone")


class SmartPhoneAction(PhoneAction):
    def buy(self):
        print("Buying a customized smartphone")
        super().buy()


class Geometry:
    # simulate method overloading with default args
    def area(self, a, b=0):
        if b == 0:
            return 3.14 * a * a  # circle area
        return a * b  # rectangle area


# MULTIPLE INHERITANCE & MRO
class ParentA:
    def buy(self):
        print("Buying from Parent A")


class ParentB:
    def buy(self):
        print("Buying from Parent B")


class HybridDevice(ParentA, ParentB):
    pass


hd = HybridDevice()
hd.buy()  # expected: Buying from Parent A (left-to-right MRO)


# ABSTRACT BASE CLASS example using abc
from abc import ABC, abstractmethod


class BankApp(ABC):
    def database(self):
        print("Connected safely to secure database cluster")

    @abstractmethod
    def security(self):
        pass


class MobileBankingApp(BankApp):
    def security(self):
        print("Biometric checking and two-factor handshake initialized")


app = MobileBankingApp()
app.database()  # prints database connection message
app.security()  # prints security initialization message
