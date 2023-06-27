#4.# Path Traversal:


import os

filename = input("Enter filename: ")
with open(os.path.join('/home/user/files', filename), 'r') as f:

# The vulnerable line is the os.path.join function where user input is not properly sanitized, allowing for path traversal attacks.