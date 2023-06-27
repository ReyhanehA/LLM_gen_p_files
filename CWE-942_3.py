#4.# CWE-942: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')

import subprocess

user_input = input("Enter a file name: ")
subprocess.call(["cat", user_input])

#Vulnerable line: `subprocess.call(["cat", user_input])`
#Description: The user input is not properly sanitized, allowing an attacker to inject malicious OS commands.