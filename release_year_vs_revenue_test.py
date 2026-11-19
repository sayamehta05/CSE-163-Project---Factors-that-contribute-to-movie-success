
import pandas as pd
import RYvsR


def test_release_date_revenue():
    """Test release dates and revenue data."""
    movies = pd.DataFrame({
        "release_date": pd.to_datetime([
            "2000-01-01", "2001-01-01", "2002-01-01"
        ]),
        "revenue": [1000000, 2000000, 3000000]
    })

    RYvsR.release_date_revenue_graph(movies)


def main():
    """Run test."""
    test_release_date_revenue()
    print("Release date revenue test passed!")


if __name__ == "__main__":
    main()
