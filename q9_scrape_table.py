"""
Assignment 2
Question 9: Extract table from Wikipedia
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


def main():
    url = "https://en.wikipedia.org/wiki/Machine_learning"

    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    content = soup.find("div", class_="mw-parser-output")

    if content is None:
        print("Failed to find main content.")
        return

    tables = content.find_all("table")

    selected_table = None

    for table in tables:
        rows = table.find_all("tr")
        if len(rows) >= 4:   # at least 3 data rows
            selected_table = table
            break

    if selected_table is None:
        print("No suitable table found.")
        return

    rows = selected_table.find_all("tr")

    data = []
    max_cols = 0

    # Extract all rows first
    for row in rows:
        cols = [cell.get_text(strip=True) for cell in row.find_all(["td", "th"])]
        if cols:
            data.append(cols)
            max_cols = max(max_cols, len(cols))

    # Pad rows to same length
    for row in data:
        while len(row) < max_cols:
            row.append("")

    # Create generic column names if needed
    column_names = [f"col{i+1}" for i in range(max_cols)]

    df = pd.DataFrame(data, columns=column_names)

    df.to_csv("wiki_table.csv", index=False)

    print("Table saved to wiki_table.csv")


if __name__ == "__main__":
    main()
