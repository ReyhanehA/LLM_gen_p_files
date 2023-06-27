#5.# Example 5: CWE-96 - Improper Neutralization of Directives in Dynamically Evaluated Code String

import json
data = input("Enter some JSON data: ")
json.loads(data) # vulnerable line

#Description: This code takes user input and directly passes it to the `json.loads()` function, which can execute arbitrary code and potentially lead to code injection attacks.