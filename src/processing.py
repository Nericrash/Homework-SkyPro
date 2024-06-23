from typing import Any

list_of_id = [
 {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(list_of_id: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция принимает список словарей и значение state и возвращающае список словарей отсортированных по state"""
    result = []
    for data in list_of_id:
        if data.get("state") == state:
            result.append(data)
    return result


def sort_by_date(list_of_id: list[dict[str, Any]], reverse_list: bool = True) -> list[dict[str, Any]]:
    """Функция сортирует словари по дате"""
    sorted_list = sorted(list_of_id, key=lambda d: d["date"], reverse=reverse_list)
    return sorted_list
