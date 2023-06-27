#8.# Example 8: CWE-209 - Information Exposure Through an Error Message

import socket

host = input("Enter a hostname: ")
port = input("Enter a port number: ")
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
except socket.error as e:
    print("Error occurred: " + str(e))

In this example, the error message printed to the console may contain sensitive information about the network connection, which could be used by an attacker to exploit the vulnerability.