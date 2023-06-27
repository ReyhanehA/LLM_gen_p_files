#3.# Example 3: CWE-209 - Information Exposure Through an Error Message

import os

filename = input("Enter a filename: ")
try:
    with open(filename, "r") as f:
        contents = f.read()
except FileNotFoundError:
    print("File not found: " + filename)
    contents = ""

In this example, the error message printed to the console may reveal the existence of sensitive files on the system.