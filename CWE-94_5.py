#6.# CWE-94: Improper Control of Generation of Code ('Code Injection')

import yaml

user_input = input("Enter a YAML string: ")
data = yaml.safe_load(user_input) # vulnerable line

#Description: This code takes user input and directly passes it to the `yaml.safe_load()` function, allowing for YAML injection.