#6.# Example 6: Improper Error Handling

import requests

url = input("Enter URL: ")

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    # #Vulnerable line: print("Error: " + str(e))
    # #Description: This code is vulnerable to improper error handling as it reveals sensitive information about the error to the user.