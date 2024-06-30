import pytest

from src.widget import get_data, mask_account_card


@pytest.fixture
def data():
    return "2018-07-11T02:26:18.671407"


def test_get_data(data):
    assert get_data(data) == "11.07.2018"


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("Visa 4567787545896213", "Visa 4567 78** **** 6213"),
        ("Счет 45161687999521344987", "Счет **4987"),
    ],
)
def test_mask_account_card(string, expected_result):
    assert mask_account_card(string) == expected_result
