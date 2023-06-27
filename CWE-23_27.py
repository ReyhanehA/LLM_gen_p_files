#8.# Example 8: CWE-23 SQL Injection

import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

query = "SELECT * FROM users WHERE username=? AND password=?"
cursor.execute(query, (username, password))

This example is similar to the previous one, but uses parameterized queries to prevent SQL injection. However, an attacker can still input a username or password with a SQL injection attack if the query is not properly constructed. The vulnerable line is `cursor.execute(query, (username, password))`.