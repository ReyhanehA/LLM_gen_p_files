#9.# Example 9: CWE-96 - Improper Neutralization of Directives in Dynamically Evaluated Code String

import base64
data = input("Enter some base64-encoded data: ")
decoded_data = base64.b64decode(data)
exec(decoded_data) # vulnerable line

#Description: This code takes user input and directly decodes it using the `base64.b64decode()` function, then executes the resulting code using the `exec()` function, which can allow an attacker to execute arbitrary code on the system.