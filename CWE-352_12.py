#5.# CWE-352: Cross-Site Request Forgery (CSRF)
# #Vulnerable line: <form action="/delete_account" method="POST">
# #Description: The form action is vulnerable to CSRF attacks as it allows an attacker to submit a request on behalf of the user without their knowledge or consent.
<form action="/delete_account" method="POST">
  <button type="submit">Delete Account</button>
</form>