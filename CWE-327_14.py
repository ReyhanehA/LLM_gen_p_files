#5.# Example 5: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import os

password = "password123"
salt = os.urandom(16)
hash_object = hashlib.sha256((password + salt).encode())
print(hash_object.hexdigest()) # vulnerable line

#Description: This code uses a weak salt which is generated using a pseudo-random number generator instead of a cryptographically secure random number generator.