#3.# Example 3: CWE-23 (Relative Path Traversal)

import os

filename = input("Enter file name: ")
if ".." in filename:
    print("Invalid file name")
else:
    filepath = os.path.join("data", filename)
    with open(filepath, "r") as f:
        data = f.read()

#Vulnerable line: None - This code is not vulnerable to relative path traversal as it checks if the `filename` input contains `..` which is used to access files outside of the intended directory.