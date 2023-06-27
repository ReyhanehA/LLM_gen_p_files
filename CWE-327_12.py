#3.# Example 3: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import hmac

message = "Hello World"
key = "secret"
hash_object = hmac.new(key.encode(), message.encode())
print(hash_object.hexdigest()) # vulnerable line

#Description: This code uses HMAC with a weak key which can be easily guessed by attackers.