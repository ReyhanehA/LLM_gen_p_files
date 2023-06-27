#2.# Code with CWE-20:

import os
filename = input("Enter a filename: ")
os.remove(filename)

#Vulnerable line: `os.remove(filename)`
#Description: This code is vulnerable to CWE-20 (Improper Input Validation) because it does not properly validate user input for the filename. An attacker can input a malicious filename that can delete important files on the system.