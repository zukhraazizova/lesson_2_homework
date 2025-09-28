import pytest
from string_utils import StringUtils

utils = StringUtils()

def test_capitalize_positive():
    assert utils.capitilize("skypro") == "Skypro"

def test_capitalize_empty():
    assert utils.capitilize("") == ""

def test_trim_spaces():
    assert utils.trim("  hello  ") == "hello"

def test_trim_no_spaces():
    assert utils.trim("world") == "world"