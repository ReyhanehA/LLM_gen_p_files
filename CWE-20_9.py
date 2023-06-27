#10.# Code with CWE-20:

import csv
filename = input("Enter a filename: ")
with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#Vulnerable line: `with open(filename, 'r') as f:`
#Description: This code is vulnerable to CWE-20 (Improper Input Validation) because it does not properly validate user input for the filename. An attacker can input a malicious filename that can read or write sensitive files on the system.