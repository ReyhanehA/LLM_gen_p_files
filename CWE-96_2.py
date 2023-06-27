#3.# Example 3: CWE-96 - Improper Neutralization of Directives in Dynamically Evaluated Code String

import subprocess
command = input("Enter a command: ")
subprocess.call(command, shell=True) # vulnerable line

#Description: This code takes user input and directly passes it to the `subprocess.call()` function with the `shell=True` option, which can allow an attacker to execute arbitrary commands on the system.