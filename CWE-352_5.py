#6.# CWE-352: Cross-Site Request Forgery (CSRF)
# #Vulnerable line: form action="/delete_post"
<form action="/delete_post" method="POST">
  <input type="hidden" name="post_id" value="123">
  <input type="submit" value="Delete Post">
</form>