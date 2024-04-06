from pathlib import Path
from src.province import Province, Tag
import pytest

TEST_PROVINCE = Path("tests/data/test_province.txt")

def test_Province():
    test_province = Province.from_txt(TEST_PROVINCE)
    
    assert test_province.owner == Tag.SWE