#2.# Example 2: CWE-209 - Information Exposure Through an Error Message

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None

In this example, the error message printed to the console may reveal that the application is vulnerable to a specific type of attack (division by zero).