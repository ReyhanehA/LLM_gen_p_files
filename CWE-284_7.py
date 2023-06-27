#8.# CWE-284: Improper Access Control
# #Vulnerable line: if user_id == comment.author_id:
# #Description: This code does not properly check if the user is authorized to delete the comment.
if user_id == comment.author_id:
    # delete comment