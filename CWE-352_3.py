#4.# CWE-352: Cross-Site Request Forgery (CSRF)
# #Vulnerable line: form action="/change_password"
<form action="/change_password" method="POST">
  <input type="password" name="new_password">
  <input type="submit" value="Change Password">
</form>