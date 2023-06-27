#7.# Example 7: CWE-23 (Relative Path Traversal)

import os

filename = input("Enter file name: ")
filepath = os.path.abspath(os.path.join("data", filename))
if not os.path.realpath(filepath).startswith(os.path.abspath("data")):
    print("Invalid file name")
else:
    with open(filepath, "r") as f:
        data = f.read()

#Vulnerable line: None - This code is not vulnerable to relative path traversal as it uses `os.path.abspath` to get the absolute path of the file, then `os.path.realpath` to get the real path of the file and checks if it starts with the absolute path of the intended directory.