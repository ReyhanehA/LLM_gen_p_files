#10.# Example 10: CWE-1004 - Unintended Execution of Code

import zipfile

filename = input("Enter a filename: ")
with zipfile.ZipFile(filename, "r") as zip:
    zip.extractall() # vulnerable line

#Description: This code takes user input for a filename and then extracts the contents of a zip file without properly validating the input. This can lead to unintended extraction of malicious files.