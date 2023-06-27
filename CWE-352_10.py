#1.# CWE-352: Cross-Site Request Forgery (CSRF)
# #Vulnerable line: form action="/transfer_funds" method="POST"
# #Description: The form action is vulnerable to CSRF attacks as it allows an attacker to submit a request on behalf of the user without their knowledge or consent.
<form action="/transfer_funds" method="POST">
  <input type="hidden" name="amount" value="1000">
  <input type="hidden" name="to_account" value="123456789">
  <button type="submit">Transfer Funds</button>
</form>