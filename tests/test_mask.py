import pytest

from src.masks import get_mask_card_number, get_mask_account
from src.widget import get_data, mask_account_card


@pytest.mark.parametrize("string, expected_result", [
    ("5499456566587896", "5499 45** **** 7896"),
    ("465656512341358", "4656 56** **** 1358")
])

def test_card_number(string, expected_result):
    assert get_mask_card_number(string) == expected_result

@pytest.mark.parametrize("string, expected_result", [
    ("45634874959948731215", "**1215"),
    ("46565656123478964789", "**4789")
])
def test_mask_account(string, expected_result):
    assert get_mask_account(string) == expected_result
