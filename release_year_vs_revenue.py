import pandas as pd
import matplotlib.pyplot as plt


def release_date_revenue_graph(movies: pd.DataFrame) -> None:
    """Compare median movie revenue across release years."""

    data = movies.copy()
    data["release_year"] = data["release_date"].dt.year

    yearly_revenue = data.groupby(
        "release_year"
    )["revenue"].median()

    plt.figure()
    plt.plot(yearly_revenue.index, yearly_revenue.values)

    plt.title("Median Worldwide Revenue by Release Year")
    plt.xlabel("Release Year")
    plt.ylabel("Median Worldwide Revenue ($)")

    plt.tight_layout()
    plt.savefig("release_date_revenue.png")
    plt.show()
    plt.close()


def main():
    """Load movie data and create release date graph."""
    movies = pd.read_csv("movies_metadata.csv", low_memory=False)

    movies["revenue"] = pd.to_numeric(
        movies["revenue"], errors="coerce"
    )

    movies["release_date"] = pd.to_datetime(
        movies["release_date"], errors="coerce"
    )

    movies = movies.dropna(
        subset=["revenue", "release_date"]
    )

    movies = movies[movies["revenue"] > 0]

    release_date_revenue_graph(movies)


if __name__ == "__main__":
    main()
