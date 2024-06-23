from src.masks import get_mask_card_number
from src.masks import get_mask_account
from datetime import datetime

def mask_account_card(number_card: str) -> str:
    """Функция маскирует номер карты/счета"""

    if "Счет" in number_card:
        mask_account = f"Счет {get_mask_account(number_card[:])}"
        return mask_account
    else:
        card = get_mask_card_number(number_card[-16:])
        mask_card_number = number_card.replace(number_card[-16:], card)
        return mask_card_number
def get_data(data: str) -> str:
    ''' Функция для работы с датой '''

    data = datetime.strptime(data, format("%Y-%m-%dT%H:%M:%S.%f"))
    return data.strftime("%d.%m.%Y")
