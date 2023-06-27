#5.# Example 5: CWE-1004 - Unintended Execution of Code

import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

table_name = input("Enter a table name: ")
cursor.execute("DROP TABLE " + table_name) # vulnerable line

#Description: This code takes user input for a table name and then executes the `DROP TABLE` command on that table without properly validating the input. This can lead to unintended deletion of tables.