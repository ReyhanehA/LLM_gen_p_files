#1.# Code with CWE-20: 

password = input("Enter your password: ")
if password == "password":
    print("Access granted!")
else:
    print("Access denied.")

#Vulnerable line: `if password == "password":`
#Description: This code is vulnerable to CWE-20 (Improper Input Validation) because it does not properly validate user input for the password. The password is hardcoded and can be easily guessed or brute-forced.