"""
Assignment 2
Question 10: Search lines containing keyword
"""


def find_lines_containing(filename, keyword):
    results = []

    with open(filename, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            if keyword.lower() in line.lower():
                results.append((line_number, line.strip()))

    return results


def main():
    matches = find_lines_containing("sample-file.txt", "lorem")

    print("Number of matching lines:", len(matches))

    for match in matches[:3]:
        print(match)


if __name__ == "__main__":
    main()
