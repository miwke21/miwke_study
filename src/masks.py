def get_mask_card_number(card_number: str) -> str:
    """
    Сокрытие номера карты.

    :param card_number: Номер карты.
    :return: Маскированный номер карты в формате '1111 11** **** 1111'.
    """
    masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return masked_card


def get_mask_account(account_number: str) -> str:
    """
    Сокрытие номера счета.

    :param account_number: Номер счета.
    :return: Маскированный номер счета в формате '**1111'.
    """
    masked_number = f"**{account_number[-4:]}"
    return masked_number
