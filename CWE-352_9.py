#10.# CWE-352: Cross-Site Request Forgery (CSRF)
# #Vulnerable line: form action="/logout"
<form action="/logout" method="POST">
  <input type="submit" value="Logout">
</form>