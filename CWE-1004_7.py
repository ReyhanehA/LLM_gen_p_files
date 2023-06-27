#8.# Example 8: CWE-1004 - Unintended Execution of Code

import csv

data = input("Enter some CSV data: ")
with open("data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(data.split(",")) # vulnerable line

#Description: This code takes user input for some CSV data and then writes it to a file using the `csv` module without properly validating the input. This can lead to unintended execution of malicious code if the input is crafted to include malicious code.