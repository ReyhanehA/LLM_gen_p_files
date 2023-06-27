#9.# Example 9: CWE-209 - Information Exposure Through an Error Message

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host = input("Enter a hostname: ")
username = input("Enter a username: ")
password = input("Enter a password: ")
try:
    ssh.connect(host, username=username, password=password)
except paramiko.AuthenticationException as e:
    print("Error occurred: " + str(e))

In this example, the error message printed to the console may contain sensitive information about the SSH connection, which could be used by an attacker to exploit the vulnerability.