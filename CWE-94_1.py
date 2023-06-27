#2.# CWE-94: Improper Control of Generation of Code ('Code Injection')

import subprocess

user_input = input("Enter a command: ")
subprocess.call(user_input) # vulnerable line

#Description: This code takes user input and directly passes it to the `subprocess.call()` function, allowing for arbitrary code execution.