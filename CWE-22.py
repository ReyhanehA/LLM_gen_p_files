#1.# CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')

import os

filename = input("Enter file name: ")
path = "/home/user/files/"

if "../" in filename:
    print("Invalid file name")
else:
    full_path = os.path.join(path, filename)
    with open(full_path, "r") as f:
        print(f.read())

In this code, the user input for the file name is not properly validated, allowing for directory traversal attacks. The vulnerable line is `if "../" in filename:`.