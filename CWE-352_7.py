#8.# CWE-352: Cross-Site Request Forgery (CSRF)
# #Vulnerable line: form action="/send_message"
<form action="/send_message" method="POST">
  <input type="text" name="recipient">
  <input type="text" name="message">
  <input type="submit" value="Send Message">
</form>