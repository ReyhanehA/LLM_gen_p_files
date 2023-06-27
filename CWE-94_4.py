#5.# CWE-94: Improper Control of Generation of Code ('Code Injection')

import json

user_input = input("Enter a JSON string: ")
data = json.loads(user_input) # vulnerable line

#Description: This code takes user input and directly passes it to the `json.loads()` function, allowing for JSON injection.