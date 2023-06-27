#2.# Example 2: CWE-23 (Relative Path Traversal)

import os

filename = input("Enter file name: ")
filepath = os.path.abspath(filename)

with open(filepath, 'r') as file:
    data = file.read()

#Vulnerable line: `filepath = os.path.abspath(filename)`
#Description: This code is vulnerable to relative path traversal because it allows an attacker to specify a file path that is outside of the intended directory by manipulating the input.