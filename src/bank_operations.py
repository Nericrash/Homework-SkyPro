import re
from collections import Counter


def get_category_counter_by_description(dictionaries: list[dict], operations: list) -> dict:
    """Принимает на вход список словарей с операциями и список строк с категориями, возвращает
    словарь, где ключи - категории, а значения - количество операций в этой категории"""
    operations_list = []
    counted = {}
    for dictionary in dictionaries:
        if dictionary["description"] in operations:
            operations_list.append(dictionary["description"])
        counted = Counter(operations_list)
    return counted


def search_by_string(dictionaries: list[dict], user_string: str) -> list[dict]:
    """Принимеает список словарей и строку поиска, возвращает список словарей, у которых в описании есть эта строка"""
    new_dict_list = []
    for dictionary in dictionaries:
        text = dictionary["description"]
        needed = re.findall(user_string, text, flags=re.IGNORECASE)
        if needed:
            new_dict_list.append(dictionary)
    return new_dict_list
