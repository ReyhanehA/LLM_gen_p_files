#4.# Code with CWE-20:

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
username = input("Enter your username: ")
password = input("Enter your password: ")
c.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password))

#Vulnerable line: `c.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password))`
#Description: This code is vulnerable to CWE-20 (Improper Input Validation) because it does not properly validate user input for the username and password. An attacker can input a malicious username or password that can execute SQL injection attacks.