import requests
import re
import time

# Start initialization phase
print("Initializing...")
t_init = time.time()

# get list of five-letter words
print('Fetching word list...')
all_words_response = requests.get("https://meaningpedia.com/5-letter-words?show=all")

# compile regex pattern
pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
# find all matches (get the words in a list)
word_list = pattern.findall(all_words_response.text)

# The current pattern in regex notation
current_pattern = re.compile(r"[a-z]i[a-z][a-z]e")

# Finish initialization phase
print(f"Initialization complete in {time.time() - t_init} seconds.")

# Start search phase
print("Searching...")
t_search = time.time()

# Get all the valid words matching the current pattern
answers = current_pattern.findall(" ".join(word_list))
print("The possible answers are:")
print(*answers, sep="\n")

# Finish search phase
print(f"Search finished in {time.time() - t_search} seconds.")
