#4.# CWE-94: Improper Control of Generation of Code ('Code Injection')

import xml.etree.ElementTree as ET

user_input = input("Enter an XML string: ")
root = ET.fromstring(user_input) # vulnerable line

#Description: This code takes user input and directly passes it to the `ET.fromstring()` function, allowing for XML injection.