#8.# Example 8: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import hashlib

password = "password123"
salt = "somesalt"
hash_object = hashlib.md5((password + salt).encode())
print(hash_object.hexdigest()) # vulnerable line

#Description: This code uses the MD5 hashing algorithm which is known to be broken and the salt is not random which makes it vulnerable to dictionary attacks.