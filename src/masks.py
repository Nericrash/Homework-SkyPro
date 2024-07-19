import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s", "%d.%m.%Y %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: list) -> str:
    """Функция принимает на вход номер карты и возвращает маскированную."""
    str_card_number = str(number_card)
    try:
        logger.info(f"Card mask: {str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}")
        return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
    except Exception:
        logger.error("Error")


def get_mask_account(account_number: list) -> str:
    """Функция принимает на вход номер счета и возвращает замаскированный"""
    str_account_number = str(account_number)
    try:
        logger.info(f"Account mask: **{str_account_number[-4:]}")
        return f"**{str_account_number[-4:]}"
    except Exception:
        logger.error("Error")
