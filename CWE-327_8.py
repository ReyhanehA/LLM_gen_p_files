#9.# Example 9: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import hashlib

password = "password123"
salt = "somesalt"
hash_object = hashlib.sha256((password + salt).encode())
print(hash_object.hexdigest()) # vulnerable line

#Description: This code uses a weak salt which is not random and can be easily guessed by attackers.