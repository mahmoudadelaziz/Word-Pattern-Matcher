import requests
import re
from itertools import permutations
import time

print("Initializing...")
t1 = time.time()

# Empty list of possible answers
answers = []

# The letters available
valid_letters = [* "qweyuipfhjkzxm"]

# The current pattern in regex notation
current_pattern = ".i..e"

# All the available permutations of available characters
char_perms = [* permutations(valid_letters, 5)]

# All permutations that match the current pattern
filtered_char_perms = [* filter(lambda x: re.search(current_pattern, "".join(x)), char_perms)]
possible_strings = ["".join(x) for x in filtered_char_perms]

print(f"Initialization complete in {time.time() - t1} seconds. \nNow searching for the possible answers...")

t2 = time.time()
# Get all the valid words among them
for possibility in possible_strings:
    # Check if this is a valid word
    response = requests.post("https://words.dev-apis.com/validate-word",
                             json = {"word": possibility},
                             timeout = 0.8)
    if response.json()['validWord'] == True:
        # if it is a valid word, add it to the list of candidate answers
        answers.append(possibility)
t3 = time.time

print("The possible answers are:\n")
print(*answers, sep="\n")
print(f"Search finished in {t3 - t2} seconds.")


## Problems with this script: Takes way too long in search, and doesn't include instances with double letters
