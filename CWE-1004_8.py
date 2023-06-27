#9.# Example 9: CWE-1004 - Unintended Execution of Code

import tarfile

filename = input("Enter a filename: ")
with tarfile.open(filename, "r") as tar:
    tar.extractall() # vulnerable line

#Description: This code takes user input for a filename and then extracts the contents of a tar file without properly validating the input. This can lead to unintended extraction of malicious files.