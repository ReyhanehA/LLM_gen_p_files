#1.# Example 1: CWE-209 - Information Exposure Through an Error Message

try:
    # some code that may raise an exception
except Exception as e:
    print("An error occurred: " + str(e))

In this example, the error message printed to the console may contain sensitive information that could be useful to an attacker.