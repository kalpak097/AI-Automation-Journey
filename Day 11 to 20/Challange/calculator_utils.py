import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def square(a):
    return a ** 2

def cube(a):
    return a ** 3

def factorial(a):
    if a < 0:
        return "Error: Factorial of negative number does not exist"
    return math.factorial(a)