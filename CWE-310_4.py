#5.# Example 5: CWE-310 - Cryptographic Issues

import os

password = input("Enter your password: ")
salt = os.urandom(16)
hash_object = hashlib.sha256((password + salt).encode())
print(hash_object.hexdigest()) # vulnerable line

#Description: This code is vulnerable to CWE-310 as it uses a weak salt to hash passwords, which can be easily guessed by attackers.