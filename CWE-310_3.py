#4.# Example 4: CWE-310 - Cryptographic Issues

import random

password = input("Enter your password: ")
salt = str(random.randint(1000, 9999))
hash_object = hashlib.sha256((password + salt).encode())
print(hash_object.hexdigest()) # vulnerable line

#Description: This code is vulnerable to CWE-310 as it uses a weak salt to hash passwords, which can be easily guessed by attackers.