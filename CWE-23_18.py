#9.# Example 9: CWE-23 (Relative Path Traversal)

import os

filename = input("Enter file name: ")
filepath = os.path.abspath(os.path.join("data", filename))
if not os.path.relpath(filepath, "data").startswith(".."):
    with open(filepath, "r") as f:
        data = f.read()
else:
    print("Invalid file name")

#Vulnerable line: None - This code is not vulnerable to relative path traversal as it uses `os.path.abspath` to get the absolute path of the file, then `os.path.relpath` to get the relative path of the file from the intended directory and checks if it starts with `..`.