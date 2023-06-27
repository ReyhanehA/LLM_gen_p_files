#2.# CWE-942: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

import sqlite3

user_input = input("Enter a username: ")
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE username = '" + user_input + "'")

#Vulnerable line: `cursor.execute("SELECT * FROM users WHERE username = '" + user_input + "'")`
#Description: The user input is not properly sanitized, allowing an attacker to inject malicious SQL commands.