import pytest
from string_utils import StringUtils


string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize(("input_str, expected"), [
    ("pride", "Pride"),
   ("rainbow bridge", "Rainbow bridge"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected
@pytest.mark.positive
@pytest.mark.parametrize(("input_str, expected"), [
    (" pride", "pride"),
   ("rainbow", "rainbow"),
    ("    python", "python"),
])

def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize(("input_str, symbol, result"), [
    ("pride", "p", True),
   ("rainbow", "bow", True),
    (" python", " ", True),
])

def test_contains_positive(input_str, symbol, result):
    res = string_utils.contains (input_str, symbol)
    assert res == result
    

@pytest.mark.positive
@pytest.mark.parametrize(("input_str, symbol, expected"), [
    ("pride", "p", "ride"),
   ("rainbow", "bow", "rain"),
    (" python", " ", "python"),
])

def test_delete_symbol(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123", "123"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected
    
@pytest.mark.negative
@pytest.mark.parametrize(("input_str, expected"), [
    ("", ""),
   ("1", "1"),
])

def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize(("input_str, symbol, result"), [
    ("", "", True),
   ("rainbow", "L", False),
    (" python", ".", False),
])

def test_contains_negative(input_str, symbol, result):
    res = string_utils.contains (input_str, symbol)
    assert res == result

@pytest.mark.negative
@pytest.mark.parametrize(("input_str, symbol, expected"), [
    ("", "", ""),
   ("rainbow", "love", "rainbow"),
    (" python", "123", " python"),
])

def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
