#8.# CWE-94: Improper Control of Generation of Code ('Code Injection')

import base64

user_input = input("Enter a base64-encoded string: ")
data = base64.b64decode(user_input) # vulnerable line

#Description: This code takes user input and directly passes it to the `base64.b64decode()` function, allowing for arbitrary code execution.