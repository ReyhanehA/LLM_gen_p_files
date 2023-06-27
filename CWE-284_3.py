#4.# CWE-284: Improper Access Control
# #Vulnerable line: if user_id in admin_ids:
# #Description: This code does not properly check if the user has the necessary permissions to access admin functionality.
if user_id in admin_ids:
    # do admin stuff