import os
from collections import defaultdict
import ast

def file_to_word_set(filename):
    with open(filename, 'r') as file:
        return {line.strip() for line in file if line.strip()}

def sort_words_by_length_to_folder(input_filename):
    output_folder = "length_sorted_anagrams"
    os.makedirs(output_folder, exist_ok=True)

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

def is_cyclic_anagram(word, words, length):
    if len(word) != length:
        return False
    word_len = len(word)
    for i in range(1, word_len):
        rotated = word[i:] + word[:i]
        if rotated in words:
            return True
    return False

def find_cyclic_groups(words, length):
    seen = set()
    cyclic_groups = []

    for word in words:
        if len(word) != length or word in seen:
            continue

        if is_cyclic_anagram(word, words, length):
            group = set()
            word_len = len(word)

            for i in range(word_len):
                rotated = word[i:] + word[:i]
                if rotated in words:
                    group.add(rotated)

            if len(group) > 1 and not group.issubset(seen):
                cyclic_groups.append(sorted(group))
                seen.update(group)

    return cyclic_groups

def process_all_length_files(sorted_folder="length_sorted_anagrams", cyclic_folder="cyclic_length_sorted_anagrams"):
    os.makedirs(cyclic_folder, exist_ok=True)

    for filename in os.listdir(sorted_folder):
        if not filename.startswith("words_len_") or not filename.endswith(".txt"):
            continue

        length = int(filename[len("words_len_"):-4])
        filepath = os.path.join(sorted_folder, filename)
        words = file_to_word_set(filepath)

        cyclic_groups = find_cyclic_groups(words, length)

        output_file = os.path.join(cyclic_folder, f"cyclic_len_{length}.txt")
        with open(output_file, 'w') as f_out:
            for group in cyclic_groups:
                f_out.write(str(group) + "\n")

def format_cyclic_anagrams_summary(
    cyclic_folder="cyclic_length_sorted_anagrams",
    output_file="cyclic_anagrams_summary.txt"
):
    groups_by_length = {}

    for filename in sorted(os.listdir(cyclic_folder)):
        if not filename.startswith("cyclic_len_") or not filename.endswith(".txt"):
            continue

        length = int(filename[len("cyclic_len_"):-4])
        filepath = os.path.join(cyclic_folder, filename)

        with open(filepath, 'r') as f:
            groups = []
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    group = ast.literal_eval(line)
                    if isinstance(group, list):
                        groups.append(group)
                except Exception:
                    pass

            groups_by_length[length] = groups

    with open(output_file, 'w') as out:
        for length in sorted(groups_by_length):
            out.write(f"length {length}:\n")
            for group in groups_by_length[length]:
                # Join the cyclic anagrams with '->' arrows
                chain = " -> ".join(group)
                out.write(chain + "\n")
            out.write("\n")

# Usage:
input_file = "Input_words/words.txt"
sort_words_by_length_to_folder(input_file)
process_all_length_files()

print("Done! Check the folders 'length_sorted_anagrams' and 'cyclic_length_sorted_anagrams'.")

format_cyclic_anagrams_summary()
print("Summary file 'cyclic_anagrams_summary.txt' created with chained cyclic anagrams.")
