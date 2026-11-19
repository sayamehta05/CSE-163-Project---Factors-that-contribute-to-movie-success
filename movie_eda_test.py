from movie_eda import get_month


def test_get_month():
    assert get_month("2020-01-01") == "01"
    assert get_month("1999-12-31") == "12"
    assert get_month("2005-07-15") == "07"


def main():
    test_get_month()
    print("All tests passed!")


if __name__ == "__main__":
    main()
