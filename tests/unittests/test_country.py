from pathlib import Path
from src.country import Country
import pytest

TEST_PROVINCE = Path("tests/data/AKS-test_country.txt")


@pytest.fixture
def test_Country():
    test_country = Country.from_txt(TEST_PROVINCE)

    return test_country


def test_circle_load_Country():
    test_country = Country.from_txt(TEST_PROVINCE)

    CIRCLE_TEST_PROVINCE_PATH = Path("tests/data/AKS-circle_country.txt")
    test_country.to_txt(CIRCLE_TEST_PROVINCE_PATH)

    circled_country = Country.from_txt(CIRCLE_TEST_PROVINCE_PATH)

    for key in test_country.__dict__.keys():
        print(key)
        if key == "starting_state":
            print(test_country.__dict__[key][0].__dict__)
            print(circled_country.__dict__[key][0].__dict__)
        assert test_country.__dict__[key] == circled_country.__dict__[key]
    