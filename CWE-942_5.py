#6.# CWE-942: Improper Neutralization of Special Elements used in an XPath Expression ('XPath Injection')

from lxml import etree

user_input = input("Enter a username: ")
xml = "<users><user><username>" + user_input + "</username></user></users>"
root = etree.fromstring(xml)
root.xpath("//user[username='" + user_input + "']")

#Vulnerable line: `root.xpath("//user[username='" + user_input + "']")`
#Description: The user input is not properly sanitized, allowing an attacker to inject malicious XPath expressions.