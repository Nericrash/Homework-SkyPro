import pytest

from src.processing import (filter_by_state,
                            sort_by_date,
                            list_of_ids)


@pytest.fixture
def test_list_ids():
    return list_of_ids


@pytest.fixture
def test_list():
    return 'EXECUTED'


def test_filter_by_state(test_list):
    assert filter_by_state(list_of_ids, state=test_list)


def test_filter_by_state_1(test_list_ids):
    assert filter_by_state(list_of_ids) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                            {'id': 939719570, 'state': 'EXECUTED',
                                             'date': '2018-06-30T02:08:58.425572'}]


def test_filter_by_state_sort(test_list_ids):
    assert sort_by_date(list_of_ids) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# def test_filter_by_state_1(test_list_1):
#     assert filter_by_state(list_of_ids) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                                              {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
#
# def test_filter_by_state_sort(test_list_1):
#     assert sort_by_date(list_of_ids) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                                           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#                                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
# @pytest.mark.parametrize("string, expected_result", [
#     ("5499456566587896", "5499 45** **** 7896"),
#     ("465656512341358", "4656 56** **** 1358")
# ])
# def test_filter_by_state(test_list_1):
#     assert filter_by_state(list_of_ids, state=test_list_1)
