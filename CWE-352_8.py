#9.# CWE-352: Cross-Site Request Forgery (CSRF)
# #Vulnerable line: form action="/create_post"
<form action="/create_post" method="POST">
  <input type="text" name="title">
  <textarea name="content"></textarea>
  <input type="submit" value="Create Post">
</form>