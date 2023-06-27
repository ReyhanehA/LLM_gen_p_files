#10.# Example 10: Cross-Site Request Forgery (CSRF)

# #Vulnerable line:
<form action="/change_password" method="POST">
    <input type="hidden" name="new_password" value="password123">
    <input type="submit" value="Change Password">
</form>

# #Description: This code is vulnerable to CSRF because it allows an attacker to submit a form on behalf of a user without their knowledge or consent.