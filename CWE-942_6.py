#7.# CWE-942: Improper Neutralization of Special Elements used in a JSON String ('JSON Injection')

import json

user_input = input("Enter a JSON string: ")
data = json.loads(user_input)

#Vulnerable line: `data = json.loads(user_input)`
#Description: The user input is not properly sanitized, allowing an attacker to inject malicious JSON strings.