#6.# CWE-284: Improper Access Control
# #Vulnerable line: if user_id == post.author_id:
# #Description: This code does not properly check if the user is authorized to edit the post.
if user_id == post.author_id:
    # edit post