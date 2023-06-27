#2.# Example 2: CWE-209 - Information Exposure Through an Error Message

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")

In this example, the error message printed to the console reveals that the input value of `b` was zero, which could be used by an attacker to exploit the vulnerability.