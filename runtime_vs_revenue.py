
import pandas as pd
import matplotlib.pyplot as plt


def load_data() -> pd.DataFrame:
    """Load and clean the movie dataset."""
    movies = pd.read_csv("movies_metadata.csv", low_memory=False)

    # Convert revenue and runtime to numeric values
    movies["revenue"] = pd.to_numeric(
        movies["revenue"], errors="coerce"
    )
    movies["runtime"] = pd.to_numeric(
        movies["runtime"], errors="coerce"
    )

    # Remove rows with missing or zero revenue
    movies = movies.dropna(subset=["revenue", "runtime"])
    movies = movies[
        (movies["revenue"] > 0) &
        (movies["runtime"] > 0)
    ].copy()

    return movies


def runtime_revenue_graph(movies: pd.DataFrame) -> None:
    """Compare movie runtime and worldwide revenue."""
    plt.figure()
    plt.scatter(movies["runtime"], movies["revenue"])

    plt.title("Movie Runtime vs. Worldwide Revenue")
    plt.xlabel("Runtime (minutes)")
    plt.ylabel("Worldwide Revenue ($)")

    plt.tight_layout()
    plt.savefig("runtime_revenue.png")
    plt.show()
    plt.close()


def main():
    """Load data, print statistics, and create graph."""
    movies = load_data()

    print("Dataset shape:", movies.shape)

    print("\nRevenue statistics:")
    print(movies["revenue"].describe())

    print("\nRuntime statistics:")
    print(movies["runtime"].describe())

    runtime_revenue_graph(movies)


if __name__ == "__main__":
    main()
