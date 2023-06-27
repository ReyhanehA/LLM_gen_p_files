#10.# Example 10: CWE-310 - Cryptographic Issues

import hashlib

password = input("Enter your password: ")
salt = hashlib.sha256(os.urandom(16)).hexdigest()
hash_object = hashlib.sha512((password + salt).encode())
print(hash_object.hexdigest()) # vulnerable line

#Description: This code is vulnerable to CWE-310 as it uses a weak salt to hash passwords, which can be easily guessed by attackers.