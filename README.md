# Anagram Finder

This program identifies and groups anagrams from a given input file.

## Design decisions

For more details, see the [Design Decisions](DESIGN_DECISION.md).

## Objective

The objective of this task is to develop a Python program that identifies and groups anagrams from a given input file. Two words are considered anagrams if they contain the same letters but in a different order (e.g., "race" and "care").

## Prerequisites

- [python](https://www.python.org/)

## How to Run

1.  **Prepare the input file:** Create or modify a text file named `sample.txt` directory as `index.py`. Each word should be on a new line. An example `sample.txt` is provided below:

    ```
    act
    cat
    tree
    race
    care
    acre
    bee
    ```

2.  **Run the program:** Open a terminal or command prompt, navigate to the directory where you saved the files, and run the following command:

    ```bash
    python index.py
    ```

## Expected Output

The program will print groups of anagrams, with words that share the same letters printed on the same line.
