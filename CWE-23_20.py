#1.# Example 1: CWE-23 Path Traversal

import os

filename = input("Enter file name: ")
filepath = "/home/user/files/" + filename
if os.path.isfile(filepath):
    with open(filepath, "r") as f:
        print(f.read())
else:
    print("File not found")

In this example, an attacker can input a filename with "../" to traverse up the directory and access files outside of the intended directory. The vulnerable line is `filepath = "/home/user/files/" + filename`.