"""
Assignment 2
Question 8: Extract H2 headings
"""

import requests
from bs4 import BeautifulSoup


def main():
    url = "https://en.wikipedia.org/wiki/Data_science"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    content = soup.find("div", class_="mw-parser-output")

    headings = []

    for h2 in content.find_all("h2"):
        title = h2.get_text().replace("[edit]", "").strip()

        if not any(word in title for word in
                   ["References", "External links", "See also", "Notes"]):
            headings.append(title)

    with open("headings.txt", "w", encoding="utf-8") as f:
        for heading in headings:
            f.write(heading + "\n")

    print("Headings saved to headings.txt")


if __name__ == "__main__":
    main()
