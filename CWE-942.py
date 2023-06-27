#1.# CWE-942: Improper Neutralization of Special Elements in a Command ('Command Injection')

import os

user_input = input("Enter a file name: ")
os.system("cat " + user_input)

#Vulnerable line: `os.system("cat " + user_input)`
#Description: The user input is not properly sanitized, allowing an attacker to inject malicious commands.