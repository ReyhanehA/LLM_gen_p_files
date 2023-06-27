#10.# Example 10: CWE-23 (Relative Path Traversal)

import os

filename = input("Enter file name: ")
filepath = os.path.abspath(os.path.join("data", filename))
if not os.path.commonpath([os.path.abspath("data"), filepath]) == os.path.abspath("data"):
    print("Invalid file name")
else:
    with open(filepath, "r") as f:
        data = f.read()

#Vulnerable line: None - This code is not vulnerable to relative path traversal as it uses `os.path.abspath` to get the absolute path of the file, then `os.path.commonpath` to get the common path of the absolute path of the intended directory and the file path and checks if it is equal to the absolute path of the intended directory.