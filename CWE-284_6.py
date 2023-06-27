#7.# CWE-284: Improper Access Control
# #Vulnerable line: if user_role == 'admin' and user_id == post.author_id:
# #Description: This code does not properly check if the user has the necessary permissions to edit the post as an admin.
if user_role == 'admin' and user_id == post.author_id:
    # edit post as admin