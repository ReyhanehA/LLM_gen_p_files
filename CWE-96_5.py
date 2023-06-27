#6.# Example 6: CWE-96 - Improper Neutralization of Directives in Dynamically Evaluated Code String

import xml.etree.ElementTree as ET
xml_data = input("Enter some XML data: ")
root = ET.fromstring(xml_data) # vulnerable line

#Description: This code takes user input and directly passes it to the `ET.fromstring()` function, which can execute arbitrary code and potentially lead to code injection attacks.