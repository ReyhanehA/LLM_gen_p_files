#3.# Example 3: CWE-209 - Information Exposure Through an Error Message

import os

filename = input("Enter a filename: ")
try:
    with open(filename, 'r') as f:
        contents = f.read()
except FileNotFoundError:
    print("File not found: " + filename)

In this example, the error message printed to the console reveals that the file specified by the user was not found, which could be used by an attacker to determine the existence of sensitive files.