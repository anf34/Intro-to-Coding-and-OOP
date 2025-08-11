import os
from collections import defaultdict

def sort_words_by_length_to_folder(input_filename):
    """
    Read words from input file, group by word length,
    sort each group alphabetically, and write each group to a separate file
    inside the folder "length_sorted_anagrams".

    Args:
        input_filename (str): Path to the input text file containing words.
    """
    output_folder = "length_sorted_anagrams"
    os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist

    length_groups = defaultdict(list)
    with open(input_filename, 'r') as file:
        for line in file:
            word = line.strip()
            if word:
                length_groups[len(word)].append(word)

    for length, words in length_groups.items():
        words_sorted = sorted(words, key=str.lower)
        output_path = os.path.join(output_folder, f"words_len_{length}.txt")
        with open(output_path, 'w') as outfile:
            for word in words_sorted:
                outfile.write(word + "\n")




def file_to_word_set(filename):
    """
    Read a text file and return a set of unique non-empty words.

    Args:
        filename (str): Path to the text file to read.

    Returns:
        set of str: A set containing all unique, non-empty stripped lines from the file.
    """
    with open(filename, 'r') as file:
        word_set = {line.strip() for line in file if line.strip()}
    return word_set

def sort_words_alphabetically(words):
    """
    Sort a list of words alphabetically (case-insensitive).

    Args:
        words (list of str): List of words to sort.

    Returns:
        list of str: New list of words sorted alphabetically.
    """
    return sorted(words, key=str.lower)


def is_cyclic_anagram(word, words, length):
    """
    Check if any cyclic permutation of `word` (excluding itself) exists in `words`.

    Args:
        word (str): The word to check.
        words (set or list of str): Collection of words to compare against.

    Returns:
        bool: True if a cyclic anagram exists, False otherwise.
    """
    word_len = len(word)
    if word_len != length:
        return False

    for i in range(1, word_len):
        rotated = word[i:] + word[:i]  # cyclic rotation
        if rotated in words:
            return True

    return False


sort_words_by_length_to_folder("Input_words/words.txt")
words = file_to_word_set("Input_words/words.txt")
cyclic_groups = []
seen = set()

for word in words:
    if word in seen:
        continue

    if is_cyclic_anagram(word, words, length=5):
        group = set()
        word_len = len(word)

        for i in range(word_len):
            rotated = word[i:] + word[:i]
            if rotated in words:
                group.add(rotated)

        if len(group) > 1 and not group.issubset(seen):
            cyclic_groups.append(sorted(group))
            seen.update(group)

print(cyclic_groups)
