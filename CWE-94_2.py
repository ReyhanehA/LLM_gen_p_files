#3.# CWE-94: Improper Control of Generation of Code ('Code Injection')

import sqlite3

user_input = input("Enter a SQL query: ")
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute(user_input) # vulnerable line

#Description: This code takes user input and directly passes it to the `cursor.execute()` function, allowing for SQL injection.