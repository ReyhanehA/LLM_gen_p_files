#7.# Example 7: CWE-209 - Information Exposure Through an Error Message

import json

data = input("Enter some JSON data: ")
try:
    parsed_data = json.loads(data)
except json.JSONDecodeError as e:
    print("An error occurred: " + str(e))

In this example, the error message printed to the console may reveal information about the application's data format.