#2.# Example 2: CWE-1004 - Unintended Execution of Code

import subprocess

command = input("Enter a command: ")
subprocess.call(command, shell=True) # vulnerable line

#Description: This code takes user input for a command and then executes it using the `subprocess` module without properly validating the input. This can lead to unintended execution of malicious code.