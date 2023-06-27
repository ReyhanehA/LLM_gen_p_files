#9.# CWE-942: Improper Neutralization of Special Elements used in a URL ('URL Injection')

import urllib.request

user_input = input("Enter a URL: ")
response = urllib.request.urlopen(user_input)

#Vulnerable line: `response = urllib.request.urlopen(user_input)`
#Description: The user input is not properly sanitized, allowing an attacker to inject malicious URLs.