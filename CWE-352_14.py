#8.# CWE-352: Cross-Site Request Forgery (CSRF)
# #Vulnerable line: <form action="/change_password" method="POST">
# #Description: The form action is vulnerable to CSRF attacks as it allows an attacker to submit a request on behalf of the user without their knowledge or consent.
<form action="/change_password" method="POST">
  <input type="password" name="new_password">
  <button type="submit">Change Password</button>
</form>