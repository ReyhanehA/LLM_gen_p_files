#5.# Example 5: CWE-23 Command Injection

import subprocess

filename = input("Enter file name: ")
subprocess.call("cat " + filename, shell=True)

In this example, an attacker can input a filename with a command to execute arbitrary code on the system. The vulnerable line is `subprocess.call("cat " + filename, shell=True)`.