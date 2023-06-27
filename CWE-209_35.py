#6.# Example 6: CWE-209 - Information Exposure Through an Error Message

import subprocess

command = input("Enter a command: ")
try:
    output = subprocess.check_output(command, shell=True)
except subprocess.CalledProcessError as e:
    print("An error occurred: " + str(e))

In this example, the error message printed to the console may reveal information about the application's system configuration.