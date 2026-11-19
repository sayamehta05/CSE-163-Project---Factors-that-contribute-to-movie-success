"""
CSE 163 Final Project
Analyzing the Factors Behind Movie Success
Authors: Saya Mehta and Camelee Yee

Analyzes movie budget, revenue, reuntime, and
release month using Pandas and Seaborn.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def get_month(date):
    """
    Takes a release data string in YYYY-MM-DD format and returns the two
    digit month as a string.
    """
    return date[5:7]


def main():
    """
    Analyzes movie data, calculates statistics,
    and creates visualizations.
    """
    df = pd.read_csv("movies_metadata.csv")
    print(df.head())
    print(len(df))

    """
    Selects the budget and revenue columns from the full
    movie dataset, then drops any row missing a value in on of those
    columns. Prints how many movies remain after removing missing data.
    """
    financial_df = df[["budget", "revenue"]]
    cleaner_financial_df = financial_df.dropna()
    print(len(cleaner_financial_df))

    """
    Counts how many movies have a budget of zero and how many have a
    revenue of zero. A value of zero probably means the number wasn't
    recorded, so those rows aren't reliable for analysis. Budget is
    compared to the string "0" because that is stored as a string.
    """
    movie_with_zero_budget = cleaner_financial_df[
        cleaner_financial_df["budget"] == "0"
    ]
    print(len(movie_with_zero_budget))
    movie_with_zero_revenue = cleaner_financial_df[
        cleaner_financial_df["revenue"] == 0
    ]
    print(len(movie_with_zero_revenue))

    """
    Keeps movies where both budget and revenue are nonzero,
    giving a dataset of movies with real financial information.
    Prints how many usable movies are left.
    """
    usable_data = cleaner_financial_df[
        (cleaner_financial_df["budget"] != "0")
        & (cleaner_financial_df["revenue"] != 0)
    ]
    print(len(usable_data))

    """
    Counts the movies with a runtime of 0 minutes, then keeps only
    movies with a runtime greater than 0. Prints summary statistics
    for runtime.
    """
    zero_runtime = df[df["runtime"] == 0]
    print(len(zero_runtime))
    cleaner_runtime = df[df["runtime"] > 0]
    print(len(cleaner_runtime))
    print(cleaner_runtime["runtime"].describe())

    longest_movies = cleaner_runtime["runtime"].max()
    print(longest_movies)

    """
    Parsing through data to compare valid runtimes agains valid
    revenues. Prints how many movies are both valid.
    """
    runtime_revenue = cleaner_runtime[cleaner_runtime["revenue"] > 0]
    print(len(runtime_revenue))

    """
    Converts the budget column from text to floats so it can
    be plotted and compared. Prints summary stats for budget
    and revenue.
    """
    usable_data["budget"] = usable_data["budget"].apply(float)
    print(usable_data[["budget", "revenue"]].describe())

    """
    Scatter plot of budget vs revenue
    """
    sns.relplot(
        data=usable_data,
        x="budget",
        y="revenue",
        kind="scatter",
    )

    plt.title("Budget vs Revenue")
    plt.xlabel("Budget ($)")
    plt.ylabel("Revenue ($)")
    plt.savefig("budget_vs_revenue.png", bbox_inches="tight")

    """
    Selects the release date and revenue columns, drops rows with missing
    values. Adds a month column using get_month, then groups the movies
    by month and prints the avg revenue for each month.
    """
    release_data = df[["release_date", "revenue"]]
    release_data = release_data.dropna()
    release_data = release_data[release_data["revenue"] > 0]
    print(len(release_data))

    release_data["month"] = release_data["release_date"].apply(get_month)
    print(release_data[["release_date", "month"]].head())
    monthly_revenue = release_data.groupby("month")["revenue"].mean()
    print(monthly_revenue)

    """
    Release time vs revenue bar chart.
    """
    sns.catplot(
        data=release_data,
        x="month",
        y="revenue",
        kind="bar"
    )

    plt.title("Average Revenue by Release Month")
    plt.xlabel("Release Month")
    plt.ylabel("Revenue ($)")
    plt.savefig("release_date_vs_revenue.png", bbox_inches="tight")


if __name__ == "__main__":
    main()
