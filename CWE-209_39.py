#10.# Example 10: CWE-209 - Information Exposure Through an Error Message

import random

def get_random_number():
    try:
        return random.randint(1, 10)
    except Exception as e:
        print("An error occurred: " + str(e))

In this example, the error message printed to the console may reveal information about the application's random number generation.