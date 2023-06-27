#9.# Example 9: CWE-209 - Information Exposure Through an Error Message

import math

x = input("Enter a number: ")
try:
    x = float(x)
    y = math.sqrt(x)
except ValueError as e:
    print("An error occurred: " + str(e))

In this example, the error message printed to the console may reveal information about the application's input validation.