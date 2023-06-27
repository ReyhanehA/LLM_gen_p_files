#6.# Example 6: CWE-23 (Relative Path Traversal)

import os

filename = input("Enter file name: ")
filepath = os.path.abspath(os.path.join("data", filename))
if not os.path.isfile(filepath):
    print("Invalid file name")
else:
    with open(filepath, "r") as f:
        data = f.read()

#Vulnerable line: None - This code is not vulnerable to relative path traversal as it uses `os.path.abspath` to get the absolute path of the file and checks if it is a file before opening it.