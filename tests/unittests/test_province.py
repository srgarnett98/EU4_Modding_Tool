from pathlib import Path
from src.province import Province
import pytest

TEST_PROVINCE = Path("tests/data/test_province.txt")


@pytest.fixture
def test_Province():
    test_province = Province.from_txt(TEST_PROVINCE)

    return test_province


def test_circle_load_Province():
    test_province = Province.from_txt(TEST_PROVINCE)

    CIRCLE_TEST_PROVINCE_PATH = Path("tests/data/circle_province.txt")

    test_province.to_txt(CIRCLE_TEST_PROVINCE_PATH)

    circled_province = Province.from_txt(CIRCLE_TEST_PROVINCE_PATH)

    for key in test_province.__dict__.keys():
        assert test_province.__dict__[key] == circled_province.__dict__[key]
