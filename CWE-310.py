#1.# Example 1: CWE-310 - Cryptographic Issues

import hashlib

password = input("Enter your password: ")
hash_object = hashlib.sha256(password.encode())
print(hash_object.hexdigest()) # vulnerable line

#Description: This code is vulnerable to CWE-310 as it uses a weak cryptographic algorithm (SHA-256) to hash passwords, which can be easily cracked by attackers.