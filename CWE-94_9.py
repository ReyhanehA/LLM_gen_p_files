#10.# CWE-94: Improper Control of Generation of Code ('Code Injection')

import ftplib

user_input = input("Enter an FTP server address: ")
ftp = ftplib.FTP(user_input) # vulnerable line

#Description: This code takes user input and directly passes it to the `ftplib.FTP()` function, allowing for arbitrary code execution.