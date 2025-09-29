import pytest
from string_utils import StringUtils

utils = StringUtils()

# ----- capitilize -----
def test_capitilize_positive():
    assert utils.capitilize("skypro") == "Skypro"

def test_capitilize_empty():
    assert utils.capitilize("") == ""

def test_capitilize_uppercase():
    assert utils.capitilize("PYTHON") == "Python"


# ----- trim -----
def test_trim_spaces():
    assert utils.trim("  hello  ") == "hello"

def test_trim_no_spaces():
    assert utils.trim("world") == "world"

def test_trim_empty():
    assert utils.trim("") == ""


# ----- to_list -----
def test_to_list_default():
    assert utils.to_list("a,b,c") == ["a", "b", "c"]

def test_to_list_custom_delimeter():
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]

def test_to_list_empty():
    assert utils.to_list("") == []


# ----- contains -----
def test_contains_true():
    assert utils.contains("hello", "e") is True

def test_contains_false():
    assert utils.contains("hello", "z") is False


# ----- delete_symbol -----
def test_delete_symbol_exist():
    assert utils.delete_symbol("hello", "l") == "heo"

def test_delete_symbol_not_exist():
    assert utils.delete_symbol("hello", "z") == "hello"


# ----- starts_with -----
def test_starts_with_true():
    assert utils.starts_with("hello", "h") is True

def test_starts_with_false():
    assert utils.starts_with("hello", "a") is False


# ----- end_with -----
def test_end_with_true():
    assert utils.end_with("hello", "o") is True

def test_end_with_false():
    assert utils.end_with("hello", "x") is False


# ----- is_empty -----
def test_is_empty_true():
    assert utils.is_empty("") is True
    assert utils.is_empty("   ") is True

def test_is_empty_false():
    assert utils.is_empty("not empty") is False