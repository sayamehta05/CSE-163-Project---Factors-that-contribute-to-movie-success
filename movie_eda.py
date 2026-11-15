import pandas as pd

def main():
    df = pd.read_csv("movies_metadata.csv")
    print(df.head())
    print(df.shape)


if __name__ == "__main__":
    main()