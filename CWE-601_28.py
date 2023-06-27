#4.# Example 4: Path Traversal

# #Vulnerable line:
with open("/var/www/html/" + filename, "r") as f:

# #Description: This code is vulnerable to path traversal because it allows a user to specify a file path that is outside of the intended directory.