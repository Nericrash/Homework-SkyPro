import pytest
from src.processing import filter_by_state, sort_by_date, list_of_ids
from src.generators import transactions

@pytest.fixture
def test_transactions():
    return transactions


@pytest.fixture
def test_list_ids():
    return list_of_ids


@pytest.fixture
def test_list():
    return 'EXECUTED'