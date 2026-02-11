"""
Assignment 2
Question 7: Scrape Wikipedia title and first paragraph
"""

import requests
from bs4 import BeautifulSoup


def main():
    url = "https://en.wikipedia.org/wiki/Data_science"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    print("Page Title:", soup.title.get_text())

    content = soup.find("div", id="mw-content-text")

    for paragraph in content.find_all("p"):
        text = paragraph.get_text(strip=True)
        if len(text) >= 50:
            print("\nFirst paragraph:")
            print(text)
            break


if __name__ == "__main__":
    main()
