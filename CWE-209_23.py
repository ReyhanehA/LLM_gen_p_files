#4.# Example 4: CWE-209 - Information Exposure Through an Error Message

import requests

url = input("Enter a URL: ")
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error occurred: " + str(e))

In this example, the error message printed to the console may contain sensitive information about the HTTP request, which could be used by an attacker to exploit the vulnerability.