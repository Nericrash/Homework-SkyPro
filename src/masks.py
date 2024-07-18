from typing import List
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/mask.log",
    filemode="w",
)

logger = logging.getLogger("mask")


def get_mask_card_number(number_card: List[int]) -> str:
    """Функция принимает на вход номер карты и возвращает маскированную."""
    str_card_number = str(number_card)
    logger.info(f"Card mask: {str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}")
    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(account_number: List[int]) -> str:
    """Функция принимает на вход номер счета и возвращает замаскированный"""
    str_account_number = str(account_number)
    logger.info(f"Account mask: **{str_account_number[-4:]}")
    return f"**{str_account_number[-4:]}"
# mask_account_number = "**" + str_account_number[-4:]
# return mask_account_number
