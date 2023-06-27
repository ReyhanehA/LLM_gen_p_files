#10.# Example 10: Cross-Site Request Forgery (CSRF)

# #Vulnerable line:
<form action="/change_password" method="POST">
    <input type="hidden" name="password" value="new_password">
    <input type="submit" value="Change Password">
</form>

# #Description: This code is vulnerable to CSRF because it does not include a CSRF token to prevent unauthorized requests.