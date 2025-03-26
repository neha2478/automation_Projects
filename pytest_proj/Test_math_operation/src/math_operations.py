#here we will create a module for math operation for py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!!")
    return a / b

def remainder_div(a, b):
    if b == 0:
        raise ValueError("Cannot calculate remainder with zero division")
    return a % b

def integer_div(a, b):
    if b == 0:
        raise ValueError("Cannot perform integer division by zero")
    return a // b

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integer!!")
    if n == 0:
        return 1
    else:
        n * factorial(n - 1)