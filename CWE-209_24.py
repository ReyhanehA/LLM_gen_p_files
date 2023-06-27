#5.# Example 5: CWE-209 - Information Exposure Through an Error Message

import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

try:
    c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = c.fetchone()
except sqlite3.Error as e:
    print("Error occurred: " + str(e))

In this example, the error message printed to the console may contain sensitive information about the SQL query, which could be used by an attacker to exploit the vulnerability.