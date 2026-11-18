from datetime import date

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#getting the month from the release date
def get_month(date):
    return date[5:7]


def main():
    df = pd.read_csv("movies_metadata.csv")
    print(df.head())
    print(len(df))

    #filtering through the dataframe to get only the budget and revenue columns and dropping the rows with missing values
    financial_df = df[["budget", "revenue", "release_date"]]
    cleaner_financial_df = financial_df.dropna()
    print(len(cleaner_financial_df))

    #filtering the cleaner_financial_df even more to get only the rows with budget and revenue not equal to zero
    movie_with_zero_budget = cleaner_financial_df[cleaner_financial_df["budget"] == "0"]
    print(len(movie_with_zero_budget))
    movie_with_zero_revenue = cleaner_financial_df[cleaner_financial_df["revenue"] == 0]
    print(len(movie_with_zero_revenue))

    #Finding usable data by excluding the rows with budget and revenue equal to zero
    usable_data = cleaner_financial_df[(cleaner_financial_df["budget"] != "0") & (cleaner_financial_df["revenue"] != 0)]
    print(len(usable_data))

    #filtering through the dataframe to get only the runtime column and dropping the rows with missing values
    zero_runtime = df[df["runtime"] == 0]
    print(len(zero_runtime))
    cleaner_runtime = df[df["runtime"] > 0]
    print(len(cleaner_runtime))
    print(cleaner_runtime["runtime"].describe())

    longest_movies = cleaner_runtime["runtime"].max()
    print(longest_movies)

    #creating graphs to visualize the data
    runtime_revenue = cleaner_runtime[cleaner_runtime["revenue"] > 0]
    print(len(runtime_revenue))

    #converting budget to numeric values
    usable_data["budget"] = usable_data["budget"].apply(float)
    print(usable_data[["budget", "revenue"]].describe())

    #scatter plot of budget vs revenue
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

    
    #group release date times by months
    release_data = df[[ "release_date", "revenue"]]
    release_data = release_data.dropna()
    release_data = release_data[release_data["revenue"] > 0]
    print(len(release_data))

    release_data["month"] = release_data["release_date"].apply(get_month)
    print(release_data[["release_date", "month"]].head())
    monthly_revenue = release_data.groupby("month")["revenue"].mean()
    print(monthly_revenue)

    #Release time vs revenue
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