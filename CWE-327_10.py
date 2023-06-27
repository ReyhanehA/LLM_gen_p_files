#1.# Example 1: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import hashlib

password = "password123"
hash_object = hashlib.md5(password.encode())
print(hash_object.hexdigest()) # vulnerable line

#Description: This code uses the MD5 hashing algorithm which is known to be broken and can be easily cracked by attackers.