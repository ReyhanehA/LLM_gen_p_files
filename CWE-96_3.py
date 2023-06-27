#4.# Example 4: CWE-96 - Improper Neutralization of Directives in Dynamically Evaluated Code String

import sqlite3
table_name = input("Enter a table name: ")
conn = sqlite3.connect('example.db')
conn.execute("DROP TABLE " + table_name) # vulnerable line

#Description: This code takes user input and directly concatenates it with a SQL query, which can allow an attacker to execute arbitrary SQL commands and potentially delete or modify data in the database.