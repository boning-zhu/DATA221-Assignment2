"""
Assignment 2
Question 1: Word frequency analysis
"""

import string
from collections import Counter


def main():
    with open("sample-file.txt", "r", encoding="utf-8") as f:
        text = f.read()

    tokens = text.split()
    cleaned_tokens = []

    for token in tokens:
        token = token.lower().strip(string.punctuation)
        if sum(c.isalpha() for c in token) >= 2:
            cleaned_tokens.append(token)

    word_counts = Counter(cleaned_tokens)

    for word, count in word_counts.most_common(10):
        print(f"{word} -> {count}")


if __name__ == "__main__":
    main()
