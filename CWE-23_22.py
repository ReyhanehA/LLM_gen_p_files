#3.# Example 3: CWE-23 Path Traversal

import os

filename = input("Enter file name: ")
filepath = os.path.abspath("/home/user/files/" + filename)
if os.path.isfile(filepath):
    with open(filepath, "r") as f:
        print(f.read())
else:
    print("File not found")

This example also uses `os.path.abspath()` to prevent path traversal. However, an attacker can still input a filename with "../" to bypass the check. The vulnerable line is `filepath = os.path.abspath("/home/user/files/" + filename)`.