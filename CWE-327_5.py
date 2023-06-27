#6.# Example 6: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import hashlib

password = "password123"
hash_object = hashlib.sha1(password.encode())
print(hash_object.hexdigest()) # vulnerable line

#Description: This code uses the SHA-1 hashing algorithm which is known to be weak and can be easily cracked by attackers.