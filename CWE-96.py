#1.# Example 1: CWE-96 - Improper Neutralization of Directives in Dynamically Evaluated Code String

user_input = input("Enter a command: ")
eval(user_input) # vulnerable line

#Description: This code takes user input and directly evaluates it using the `eval()` function, which can execute arbitrary code and potentially lead to code injection attacks.