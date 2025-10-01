import pytest
from string_utils import StringUtils

utils = StringUtils()

# --- capitalize ---
def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"

def test_capitalize_empty():
    assert utils.capitalize("") == ""

def test_capitalize_already_capitalized():
    assert utils.capitalize("Skypro") == "Skypro"

# --- trim ---
def test_trim_spaces():
    assert utils.trim("   skypro") == "skypro"

def test_trim_no_spaces():
    assert utils.trim("skypro") == "skypro"

def test_trim_only_spaces():
    assert utils.trim("     ") == ""

# --- contains ---
def test_contains_true():
    assert utils.contains("SkyPro", "S") is True

def test_contains_false():
    assert utils.contains("SkyPro", "U") is False

def test_contains_empty_string():
    assert utils.contains("", "a") is False

# --- delete_symbol ---
def test_delete_symbol_single_char():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"

def test_delete_symbol_substring():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

def test_delete_symbol_not_found():
    assert utils.delete_symbol("SkyPro", "x") == "SkyPro"

def test_delete_symbol_empty_string():
    assert utils.delete_symbol("", "x") == ""