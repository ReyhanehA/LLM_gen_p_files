#3.# CWE-942: Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection')

import ldap

user_input = input("Enter a username: ")
conn = ldap.initialize('ldap://localhost')
conn.simple_bind_s("cn=admin,dc=example,dc=com", "password")
conn.search("dc=example,dc=com", "(uid=" + user_input + ")")

#Vulnerable line: `conn.search("dc=example,dc=com", "(uid=" + user_input + ")")`
#Description: The user input is not properly sanitized, allowing an attacker to inject malicious LDAP queries.