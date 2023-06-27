#4.# Example 4: CWE-23 Path Traversal

import os

filename = input("Enter file name: ")
filepath = os.path.abspath(os.path.join("/home/user/files/", filename))
if os.path.isfile(filepath):
    with open(filepath, "r") as f:
        print(f.read())
else:
    print("File not found")

This example combines the previous two examples by using both `os.path.abspath()` and `os.path.join()` to prevent path traversal. However, an attacker can still input a filename with "../" to bypass the check. The vulnerable line is `filepath = os.path.abspath(os.path.join("/home/user/files/", filename))`.