"""
Assignment 2
Question 6: Crime risk categorization
"""

import pandas as pd


def main():
    df = pd.read_csv("crime.csv")

    df["risk"] = df["ViolentCrimesPerPop"].apply(
        lambda x: "HighCrime" if x >= 0.5 else "LowCrime"
    )

    grouped = df.groupby("risk")["PctUnemployed"].mean()

    for risk_level, avg_unemployment in grouped.items():
        print(f"{risk_level}: Average Unemployment = {avg_unemployment:.4f}")


if __name__ == "__main__":
    main()
