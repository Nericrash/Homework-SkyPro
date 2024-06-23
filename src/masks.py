from typing import List


def get_mask_card_number(number_card: List[int]) -> str:
    """Функция принимает на вход номер карты и возвращает маскированную."""
    str_card_number = str(number_card)
    mask_card_number = str_card_number[:4] + " " + str_card_number[4:6] + "** **** " + str_card_number[-4:]
    return mask_card_number


def get_mask_account(account_number: List[int]) -> str:
    """Функция принимает на вход номер счета и возвращает замаскированный"""
    str_account_number = str(account_number)
    mask_account_number = "**" + str_account_number[-4:]
    return mask_account_number
