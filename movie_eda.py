import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("movies_metadata.csv")
    print(df.head())
    print(len(df))

    #filtering through the dataframe to get only the budget and revenue columns and dropping the rows with missing values
    financial_df = df[["budget", "revenue"]]
    cleaner_financial_df = financial_df.dropna()
    print(len(cleaner_financial_df))

    #filtering through the dataframe to get only the rows with budget and revenue equal to zero
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
    #1. 
    runtime_revenue = cleaner_runtime[cleaner_runtime["revenue"] > 0]
    print(len(runtime_revenue))

    #converting budget to numeric values
    usable_data["budget"] = usable_data["budget"].apply(float)
    print(usable_data[["budget", "revenue"]].describe())

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

if __name__ == "__main__":
    main()