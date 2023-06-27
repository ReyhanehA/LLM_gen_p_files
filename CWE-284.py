#1.# CWE-284: Improper Access Control
# #Vulnerable line: if user_role == 'admin':
# #Description: This code does not properly check if the user has the necessary permissions to access admin functionality.
if user_role == 'admin':
    # do admin stuff