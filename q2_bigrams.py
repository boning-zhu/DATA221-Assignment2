"""
Assignment 2
Question 2: Bigram frequency analysis
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

    bigrams = []
    for i in range(len(cleaned_tokens) - 1):
        bigrams.append(f"{cleaned_tokens[i]} {cleaned_tokens[i+1]}")

    bigram_counts = Counter(bigrams)

    for bigram, count in bigram_counts.most_common(5):
        print(f"{bigram} -> {count}")


if __name__ == "__main__":
    main()
