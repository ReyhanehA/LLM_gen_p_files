#10.# CWE-284: Improper Access Control
# #Vulnerable line: if user_id == session['user_id'] and request.method == 'POST':
# #Description: This code does not properly check if the user is authorized to submit a POST request.
if user_id == session['user_id'] and request.method == 'POST':
    # submit form data