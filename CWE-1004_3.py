#4.# Example 4: CWE-1004 - Unintended Execution of Code

import json

data = input("Enter some data: ")
with open("data.json", "w") as f:
    json.dump(data, f) # vulnerable line

#Description: This code takes user input for some data and then writes it to a JSON file without properly validating the input. This can lead to unintended execution of malicious code if the input is crafted to include malicious code.