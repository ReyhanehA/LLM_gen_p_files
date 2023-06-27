#7.# CWE-352: Cross-Site Request Forgery (CSRF)
# #Vulnerable line: form action="/update_profile"
<form action="/update_profile" method="POST">
  <input type="text" name="username">
  <input type="submit" value="Update Profile">
</form>