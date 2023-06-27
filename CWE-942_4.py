#5.# CWE-942: Improper Neutralization of Special Elements used in a Regular Expression ('Regular Expression Injection')

import re

user_input = input("Enter a string: ")
pattern = re.compile(user_input)

#Vulnerable line: `pattern = re.compile(user_input)`
#Description: The user input is not properly sanitized, allowing an attacker to inject malicious regular expressions.