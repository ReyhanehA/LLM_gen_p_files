#6.# Example 6: CWE-1004 - Unintended Execution of Code

import xml.etree.ElementTree as ET

xml_data = input("Enter some XML data: ")
root = ET.fromstring(xml_data) # vulnerable line

#Description: This code takes user input for some XML data and then parses it using the `xml.etree.ElementTree` module without properly validating the input. This can lead to unintended execution of malicious code if the input is crafted to include malicious code.