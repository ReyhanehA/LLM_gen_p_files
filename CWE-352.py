#1.# CWE-352: Cross-Site Request Forgery (CSRF)
# #Vulnerable line: form action="/transfer_funds"
<form action="/transfer_funds" method="POST">
  <input type="hidden" name="amount" value="1000">
  <input type="submit" value="Transfer Funds">
</form>