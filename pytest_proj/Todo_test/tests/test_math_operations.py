import pytest 
import sys 
import os

#Adding src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from math_operations import add, subtract, multiply, divide, remainder_div, integer_div, factorial

#Test Addition
def test_add():
    assert add(3, 5) == 8
    assert add(-3, 5) == 2
    assert add(0, 0) == 0

#Test Subtract
def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5
    assert subtract(0, 0) == 0

#Test Multiply
def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-4, 3) == -12
    assert multiply(0, 3) == 0

#Test Divide 
def test_divide():
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5

#Test exception for divide by zero
def test_divide_by_zero():
    with pytest.raises(ValueError, match = "Cannot divide by zero!!"):
        divide(10, 0)

#Test Reminder Division 
def test_reminder_div():
    assert remainder_div(10, 3) == 1
    assert remainder_div(15, 4) == 3
    assert remainder_div(-10, 3) == -1

#Test exception for remainder division by zero
def test_remainder_div_by_zero():
    with pytest.raises(ValueError, match="Cannot calculate remainder with zero division"):
        remainder_div(10, 0)

#Test Integer Division
def test_integer_div():
    assert integer_div(10, 3) == 3
    assert integer_div(15, 4) == 3
    assert integer_div(-10, 3) == -4

# Test exception for integer division by zero
def test_integer_div_by_zero():
    with pytest.raises(ValueError, match="Cannot perform integer division by zero"):
        integer_div(10, 0)

#Test Factorial
def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1

#Test exception for invalid factorial inputs
def test_factorial_invalid():
    with pytest.raises(ValueError, match="Factorial is only defined for non-negative integer!!"):
        factorial(-5)
    with pytest.raises(ValueError, match="Factorial is only defined for non-negative integer!!"):
        factorial(2.5)

