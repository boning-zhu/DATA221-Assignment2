"""
Assignment 2
Question 9: Extract table from Wikipedia
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


def main():
    url = "https://en.wikipedia.org/wiki/Machine_learning"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    content = soup.find("div", id="mw-content-text")
    tables = content.find_all("table")

    selected_table = None

    for table in tables:
        rows = table.find_all("tr")
        if len(rows) >= 4:
            selected_table = table
            break

    rows = selected_table.find_all("tr")

    headers = [th.get_text(strip=True) for th in rows[0].find_all("th")]

    if not headers:
        headers = [f"col{i+1}" for i in range(len(rows[1].find_all("td")))]

    data = []

    for row in rows[1:]:
        cols = [cell.get_text(strip=True) for cell in row.find_all(["td", "th"])]

        while len(cols) < len(headers):
            cols.append("")

        data.append(cols)

    df = pd.DataFrame(data, columns=headers)
    df.to_csv("wiki_table.csv", index=False)

    print("Table saved to wiki_table.csv")


if __name__ == "__main__":
    main()
