#1.# Example 1: CWE-23 (Relative Path Traversal)

import os

filename = input("Enter file name: ")
filepath = os.path.join("data", filename)
with open(filepath, "r") as f:
    data = f.read()

#Vulnerable line: `filepath = os.path.join("data", filename)` - This code is vulnerable to relative path traversal as it allows an attacker to manipulate the `filename` input to access files outside of the intended directory.