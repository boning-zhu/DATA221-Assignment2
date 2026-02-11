"""
Assignment 2
Question 5: Grade band summary
"""

import pandas as pd


def assign_band(grade):
    if grade <= 9:
        return "Low"
    elif grade <= 14:
        return "Medium"
    else:
        return "High"


def main():
    df = pd.read_csv("student.csv")

    df["grade_band"] = df["grade"].apply(assign_band)

    summary = df.groupby("grade_band").agg(
        number_of_students=("grade", "count"),
        average_absences=("absences", "mean"),
        internet_percentage=("internet", "mean")
    )

    summary["internet_percentage"] *= 100

    summary.to_csv("student_bands.csv")

    print(summary)


if __name__ == "__main__":
    main()
