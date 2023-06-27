#5.# Example 5: CWE-209 - Information Exposure Through an Error Message

import sqlite3

conn = sqlite3.connect("mydatabase.db")
try:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
except sqlite3.Error as e:
    print("An error occurred: " + str(e))

In this example, the error message printed to the console may reveal information about the application's database schema.