#7.# Example 7: CWE-209 - Information Exposure Through an Error Message

import subprocess

command = input("Enter a command: ")
try:
    output = subprocess.check_output(command, shell=True)
except subprocess.CalledProcessError as e:
    print("Error occurred: " + str(e))

In this example, the error message printed to the console may contain sensitive information about the command executed, which could be used by an attacker to exploit the vulnerability.