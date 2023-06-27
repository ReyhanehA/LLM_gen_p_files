#3.# CWE-352: Cross-Site Request Forgery (CSRF)
# #Vulnerable line: <a href="/delete_account">Delete Account</a>
# #Description: The link is vulnerable to CSRF attacks as it allows an attacker to submit a request on behalf of the user without their knowledge or consent.
<a href="/delete_account">Delete Account</a>