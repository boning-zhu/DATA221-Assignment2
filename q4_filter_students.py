"""
Assignment 2
Question 4: Filter high engagement students
"""

import pandas as pd


def main():
    df = pd.read_csv("student.csv")

    filtered = df[
        (df["studytime"] >= 3) &
        (df["internet"] == 1) &
        (df["absences"] <= 5)
    ]

    filtered.to_csv("high_engagement.csv", index=False)

    print("Students saved:", len(filtered))
    print("Average grade:", filtered["grade"].mean())


if __name__ == "__main__":
    main()
