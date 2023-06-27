#3.# CWE-209: Information Exposure Through an Error Message
# #Vulnerable line: print("Error: " + str(e))
try:
    # some code that may raise an exception
except Exception as e:
    print("Error: " + e.__class__.__name__)