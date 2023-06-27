#2.# CWE-284: Improper Access Control
# #Vulnerable line: if user_id == session['user_id']:
# #Description: This code does not properly check if the user is authorized to access the requested resource.
if user_id == session['user_id']:
    # access resource