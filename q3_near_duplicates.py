"""
Assignment 2
Question 3: Near-duplicate line detection
"""

import string
from collections import defaultdict


def normalize(line):
    line = line.lower()
    return "".join(
        c for c in line if c not in string.punctuation and not c.isspace()
    )


def main():
    groups = defaultdict(list)

    with open("sample-file.txt", "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            key = normalize(line)
            groups[key].append((line_number, line.strip()))

    duplicate_sets = [group for group in groups.values() if len(group) > 1]

    print("Number of near-duplicate sets:", len(duplicate_sets))

    for group in duplicate_sets[:2]:
        print("\nSet:")
        for line_number, text in group:
            print(f"{line_number}: {text}")


if __name__ == "__main__":
    main()
