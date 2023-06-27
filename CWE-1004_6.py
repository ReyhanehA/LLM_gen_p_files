#7.# Example 7: CWE-1004 - Unintended Execution of Code

import yaml

data = input("Enter some YAML data: ")
with open("data.yaml", "w") as f:
    yaml.dump(data, f) # vulnerable line

#Description: This code takes user input for some YAML data and then writes it to a file without properly validating the input. This can lead to unintended execution of malicious code if the input is crafted to include malicious code.