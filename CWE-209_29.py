#10.# Example 10: CWE-209 - Information Exposure Through an Error Message

import urllib.request

url = input("Enter a URL: ")
try:
    response = urllib.request.urlopen(url)
except urllib.error.URLError as e:
    print("Error occurred: " + str(e))

In this example, the error message printed to the console may contain sensitive information about the HTTP request, which could be used by an attacker to exploit the vulnerability.