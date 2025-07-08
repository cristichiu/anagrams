from collections import defaultdict

def get_char_counts(word):
    counts = defaultdict(int)
    for char in word:
        counts[char] += 1
    return counts

def grup_anagrams(filepath):
    anagram_groups = defaultdict(list)
    with open(filepath, 'r') as f:
        for line in f:
            word = line.strip()
            if word:
                char_counts = get_char_counts(word)
                key = frozenset(char_counts.items())
                anagram_groups[key].append(word)
    return anagram_groups

def display_anagram_groups(anagram_groups):
    for canonical_key, words_in_group in anagram_groups.items():
        if len(words_in_group) > 0:
            print(" ".join(words_in_group))

grups = grup_anagrams("sample.txt")
display_anagram_groups(grups)
