#9.# CWE-94: Improper Control of Generation of Code ('Code Injection')

import urllib.request

user_input = input("Enter a URL: ")
response = urllib.request.urlopen(user_input) # vulnerable line

#Description: This code takes user input and directly passes it to the `urllib.request.urlopen()` function, allowing for arbitrary code execution.