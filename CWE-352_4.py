#5.# CWE-352: Cross-Site Request Forgery (CSRF)
# #Vulnerable line: form action="/add_friend"
<form action="/add_friend" method="POST">
  <input type="text" name="friend_name">
  <input type="submit" value="Add Friend">
</form>