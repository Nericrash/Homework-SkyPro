import pytest

from src.generators import transactions
from src.processing import list_of_ids


@pytest.fixture
def test_transactions():
    return transactions


@pytest.fixture
def test_list_ids():
    return list_of_ids


@pytest.fixture
def test_list():
    return "EXECUTED"


@pytest.fixture
def test_info_csv():
    return {'date': '2023-09-05T11:30:32Z',
            'description': 'Перевод организации',
            'from': 'Счет 45803664561298323844',
            'id': '650703',
            'operationAmount': {'amount': '16210',
                                'currency': {'code': 'PEN', 'name': 'Sol'}},
            'state': 'EXECUTED',
            'to': 'Счет 45803664561298323844'}


@pytest.fixture
def test_info_xlcx():
    return {'date': '2023-09-05T11:30:32Z',
            'description': 'Перевод организации',
            'from': 'Счет 58803664561298323391',
            'id': float(650703.0),
            'operationAmount': {'amount': float(16210.0),
                                'currency': {'code': 'PEN', 'name': 'Sol'}},
            'state': 'EXECUTED',
            'to': 'Счет 39745660563456619397'}
