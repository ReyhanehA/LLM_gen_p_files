#8.# Example 8: CWE-310 - Cryptographic Issues

import hashlib

password = input("Enter your password: ")
hash_object = hashlib.sha512(password.encode())
print(hash_object.hexdigest()) # vulnerable line

#Description: This code is vulnerable to CWE-310 as it uses a strong cryptographic algorithm (SHA-512) to hash passwords, but it does not use a salt, which can make it vulnerable to dictionary attacks.