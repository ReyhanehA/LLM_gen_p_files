#3.# Example 3: CWE-1004 - Unintended Execution of Code

import pickle

data = input("Enter some data: ")
with open("data.pickle", "wb") as f:
    pickle.dump(data, f) # vulnerable line

#Description: This code takes user input for some data and then pickles it to a file without properly validating the input. This can lead to unintended execution of malicious code if the input is crafted to include malicious code.