#10.# Example 10: CWE-96 - Improper Neutralization of Directives in Dynamically Evaluated Code String

import urllib.request
url = input("Enter a URL: ")
response = urllib.request.urlopen(url)
content = response.read()
exec(content) # vulnerable line

#Description: This code takes user input and directly passes it to the `urllib.request.urlopen()` function, then executes the resulting content using the `exec()` function, which can allow an attacker to execute arbitrary code on the system.