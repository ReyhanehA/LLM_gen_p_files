#10.# CWE-942: Improper Neutralization of Special Elements used in a HTML Attribute ('HTML Injection')

from bs4 import BeautifulSoup

user_input = input("Enter an HTML tag: ")
soup = BeautifulSoup("<div>" + user_input + "</div>", "html.parser")

#Vulnerable line: `soup = BeautifulSoup("<div>" + user_input + "</div>", "html.parser")`
#Description: The user input is not properly sanitized, allowing an attacker to inject malicious HTML attributes.