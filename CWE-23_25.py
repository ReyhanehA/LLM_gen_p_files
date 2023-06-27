#6.# Example 6: CWE-23 Command Injection

import subprocess

filename = input("Enter file name: ")
subprocess.call(["cat", filename])

This example is similar to the previous one, but uses a list of arguments instead of a string to prevent command injection. However, an attacker can still input a filename with a command to execute arbitrary code on the system. The vulnerable line is `subprocess.call(["cat", filename])`.