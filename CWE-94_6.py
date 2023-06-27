#7.# CWE-94: Improper Control of Generation of Code ('Code Injection')

import pickle

user_input = input("Enter a pickled object: ")
data = pickle.loads(user_input) # vulnerable line

#Description: This code takes user input and directly passes it to the `pickle.loads()` function, allowing for arbitrary code execution.