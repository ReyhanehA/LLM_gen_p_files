#2.# Example 2: CWE-23 (Relative Path Traversal)

import os

filename = input("Enter file name: ")
filepath = os.path.abspath(os.path.join("data", filename))
with open(filepath, "r") as f:
    data = f.read()

#Vulnerable line: `filepath = os.path.abspath(os.path.join("data", filename))` - This code is still vulnerable to relative path traversal as it only uses `os.path.abspath` to get the absolute path of the file, but does not validate if the file is within the intended directory.