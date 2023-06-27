#3.# Code with CWE-20:

import requests
url = input("Enter a URL: ")
response = requests.get(url)
print(response.text)

#Vulnerable line: `response = requests.get(url)`
#Description: This code is vulnerable to CWE-20 (Improper Input Validation) because it does not properly validate user input for the URL. An attacker can input a malicious URL that can execute arbitrary code or steal sensitive information.