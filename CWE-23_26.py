#7.# Example 7: CWE-23 SQL Injection

import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
cursor.execute(query)

In this example, an attacker can input a username or password with a SQL injection attack to bypass authentication or access sensitive data. The vulnerable line is `query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"`.