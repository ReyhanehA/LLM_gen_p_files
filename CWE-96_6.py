#7.# Example 7: CWE-96 - Improper Neutralization of Directives in Dynamically Evaluated Code String

import yaml
data = input("Enter some YAML data: ")
yaml.safe_load(data) # vulnerable line

#Description: This code takes user input and directly passes it to the `yaml.safe_load()` function, which can execute arbitrary code and potentially lead to code injection attacks.