# Word Pattern Matcher

This repository contains a Python script that matches word patterns. It's a simple yet powerful tool that can help you find words that match a specific pattern. The script uses a pickled file containing a set of words, and a regular expression pattern provided by the user to find matching words.

## Files in this Repository

1. `word_pattern_matcher.py`: This is the main Python script that performs the pattern matching.
2. `wordSet.pickle`: This is a pickled file that contains a set of words used for pattern matching.

## How to Use

The Python script `word_pattern_matcher.py` is designed to be run from the command line. Here's how to use it:

1. Run the script in your terminal.
2. When prompted, enter the part of the word you currently have, replacing empty positions with dots. For example, if you're looking for a word that starts with 'th', ends with 'k', and has two unknown letters in between, you would enter `th..k`.
3. The script will then search through the set of words in the `wordSet.pickle` file and print out all words that match the pattern you entered.
4. The script also prints out the time it took to find the matching words.

## Requirements

This script requires Python 3 and the following Python libraries installed:

- `re`: This is the regular expression library in Python, used to match the pattern entered by the user.
- `time`: This library is used to calculate the time it took to find the matching words.
- `pickle`: This library is used to load the set of words from the pickled file.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue.
