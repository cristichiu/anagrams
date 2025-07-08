### Design Decisions

The chosen approach for the Anagram Finder program is based on generating a unique key for each word by counting the frequency of its characters. Two words are considered anagrams if they contain the same letters but in a different order. This means they must have the exact same character counts.

**get_char_counts:**

- This function takes the word and counts every letter storing it in a defaultdict.
- At the end it returns a dictionary that will look like this (ex. { a: 2, b: 1, c: 1 })

**grup_anagrams:**

- It reads a file line by line, every word will get through get_char_counts function.
- It creates then a key based on the dictionary returned by get_char_counts function using frozenset.
- I used frozenset because it can be used as a key in a dictionary and also the order does not metter, (ex. { a: 1, b: 1 } is exactly the same with { b: 1, a: 1 }), in this case the only thing that can make these different is the number of every key or different letters, exactly what we need.
- At the end we store every word based on the key in an array.
- This function returns a dictionary with grups of words for every key.

**display_anagram_grups:**

- This function takes the return of grup_anagrams and prints each group of anagrams on a separate line, with words separated by spaces.

### Maintainability:

- Modularity, the code is divided into clear and small functions.
- Clarity, the logic for idetifying anagrams is explicit and easy to fallow.

### Time complexity:

- For a word of length L, counting chars takes O(L) time
- Reading the file is O(Total chars)
- Dictionary append is O(1)
- To summarise the time is about O((L_avg + 1) \* M), M is the number of lines

### External libraries:

- defaultdict from collections
- Justification: defaultdict simplifies the grouping process by automatically creating an empty list for a new key if it doesn't exist, eliminating the need for explicit if key not in dict: checks. This contributes to cleaner and more concise code without adding external dependencies.

### Scalability considerations:

- For 10 million words: In average it would calculate over 70 million characters, this amount of data would likely fit in a modern PC. Processing time will take a noticebla amount of time (minute or even hours depeding on hardware specifications)
- For 100 bilion words: It would require a totaly different approach, for this amount of data we can't use this program.
- Distributed processing framework: a framework that is designed to work with datasets that are too large to fit into the memory of one machine.
