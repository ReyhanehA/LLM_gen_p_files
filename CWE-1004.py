#1.# Example 1: CWE-1004 - Unintended Execution of Code

import os

filename = input("Enter a filename: ")
os.system("rm " + filename) # vulnerable line

#Description: This code takes user input for a filename and then executes the `rm` command on that file without properly validating the input. This can lead to unintended deletion of files.