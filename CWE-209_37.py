#8.# Example 8: CWE-209 - Information Exposure Through an Error Message

import xml.etree.ElementTree as ET

xml_data = input("Enter some XML data: ")
try:
    root = ET.fromstring(xml_data)
except ET.ParseError as e:
    print("An error occurred: " + str(e))

In this example, the error message printed to the console may reveal information about the application's data format.