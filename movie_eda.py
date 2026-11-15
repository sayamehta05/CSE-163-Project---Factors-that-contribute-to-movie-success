import pandas as pd

def main():
    df = pd.read_csv("movies_metadata.csv")
    print(df.head())
    print(len(df))
    financial_df = df[["budget", "revenue"]]
    cleaner_financial_df = financial_df.dropna()
    print(len(cleaner_financial_df))
    movie_with_zero_budget = cleaner_financial_df[cleaner_financial_df["budget"] == "0"]
    print(len(movie_with_zero_budget))
    movie_with_zero_revenue = cleaner_financial_df[cleaner_financial_df["revenue"] == 0]
    print(len(movie_with_zero_revenue))


if __name__ == "__main__":
    main()