#8.# CWE-942: Improper Neutralization of Special Elements used in a Shell Command ('Shell Injection')

import shlex

user_input = input("Enter a command: ")
args = shlex.split(user_input)
subprocess.call(args)

#Vulnerable line: `args = shlex.split(user_input)`
#Description: The user input is not properly sanitized, allowing an attacker to inject malicious shell commands.