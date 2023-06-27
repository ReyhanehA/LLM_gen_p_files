#2.# Example 2: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import base64

password = "password123"
encoded_password = base64.b64encode(password.encode())
print(encoded_password) # vulnerable line

#Description: This code uses base64 encoding which is not a secure way to store passwords as it can be easily decoded by attackers.