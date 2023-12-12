import re
import time
import pickle

# Function to load the list from the pickled file
def load_set_from_pickle(file_name):
    try:
        with open(file_name, 'rb') as file:
            loaded_set = pickle.load(file)
            return loaded_set
    except FileNotFoundError:
        print("File not found.")
        return None
    except pickle.PickleError:
        print("Error loading pickled file.")
        return None

# The current pattern in regex notation
current_attempt = input(">> Enter the part of the word you currently have, replacing empty positions with dots, like the pattern (th.nk) for example.\n>> ")
current_pattern = re.compile(f"{current_attempt.lower().replace('.', '[a-z]')}")

# File name containing the pickled list
file_name = f"{len(current_attempt)}-letter-wordSet.pickle"
# Loading the list from the pickled file
word_set = load_set_from_pickle(file_name)

# Start search phase
print("\nSearching...")
t_search = time.time()

# Get all the valid words matching the current pattern
candidate_answers = {word for word in word_set if current_pattern.fullmatch(word)}
print("The possible answers are:")
print(*candidate_answers, sep="\n")

# Finish search phase
print(f"\nSearch finished in {time.time() - t_search:.3f} seconds.")
