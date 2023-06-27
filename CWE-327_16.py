#7.# Example 7: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import hashlib

password = "password123"
hash_object = hashlib.sha512(password.encode())
print(hash_object.hexdigest()) # vulnerable line

#Description: This code uses the SHA-512 hashing algorithm which is secure but the password is not salted which makes it vulnerable to dictionary attacks.