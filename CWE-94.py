#1.# CWE-94: Improper Control of Generation of Code ('Code Injection')

import os

user_input = input("Enter a command: ")
os.system(user_input) # vulnerable line

#Description: This code takes user input and directly passes it to the `os.system()` function, allowing for arbitrary code execution.