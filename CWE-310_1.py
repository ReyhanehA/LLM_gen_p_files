#2.# Example 2: CWE-310 - Cryptographic Issues

import base64

message = input("Enter your message: ")
encoded_message = base64.b64encode(message.encode())
print(encoded_message.decode()) # vulnerable line

#Description: This code is vulnerable to CWE-310 as it uses base64 encoding, which is not a secure way to protect sensitive data as it can be easily decoded by attackers.