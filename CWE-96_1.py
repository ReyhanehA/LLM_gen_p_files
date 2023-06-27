#2.# Example 2: CWE-96 - Improper Neutralization of Directives in Dynamically Evaluated Code String

import os
filename = input("Enter a filename: ")
os.system("rm " + filename) # vulnerable line

#Description: This code takes user input and directly concatenates it with a system command, which can allow an attacker to execute arbitrary commands on the system.