#6.# Example 6: CWE-209 - Information Exposure Through an Error Message

import json

data = input("Enter some JSON data: ")
try:
    json_data = json.loads(data)
except json.JSONDecodeError as e:
    print("Error occurred: " + str(e))

In this example, the error message printed to the console may contain sensitive information about the JSON data, which could be used by an attacker to exploit the vulnerability.