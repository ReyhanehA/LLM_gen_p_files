#3.# Example 3: CWE-310 - Cryptographic Issues

import hmac

message = input("Enter your message: ")
key = input("Enter your key: ")
hmac_object = hmac.new(key.encode(), message.encode())
print(hmac_object.hexdigest()) # vulnerable line

#Description: This code is vulnerable to CWE-310 as it uses a weak key to generate a message authentication code (MAC), which can be easily guessed by attackers.