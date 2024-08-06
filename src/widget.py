from masks import get_mask_card_number, get_mask_account

def mask_account_card(data: str) -> str:
    """
    Удаляет все символы кроме цифр из строки.

    :param input_string: Входная строка с буквенными символами и цифрами.
    :return: Строка, содержащая только цифры.
    """
    cleaned_card_number = ''.join(filter(str.isdigit, data))
    card_or_account = ' '.join(data.split()[:-1])
    if len(cleaned_card_number) > 16:
        return f"{card_or_account} {get_mask_account(cleaned_card_number)}"
    else:
        return f"{card_or_account} {get_mask_card_number(cleaned_card_number)}"


def get_date(date_str: str) -> str:
    """
    Дата из формата "ГГГГ-ММ-ДДTчч:мм:сс.мс" в формат "ДД.ММ.ГГГГ".

    :param date_str: Дата в формате "ГГГГ-ММ-ДДTчч:мм:сс.мс".
    :return: Дата в формате "ДД.ММ.ГГГГ".
    """
    from datetime import datetime

    date_object = datetime.strptime(date_str[:10], "%Y-%m-%d")
    formatted_date = date_object.strftime("%d.%m.%Y")
    return formatted_date


masked_card1 = input("Введите номер карты: ")
masked_card1 = mask_account_card(masked_card1)
print(masked_card1)


masked_card2 = input("Введите номер счета: ")
masked_card2 = mask_account_card(masked_card2)
print(masked_card2)


incorrect_time = input("Введите время: ")
corrected_time = get_date(incorrect_time)
print(f"Время в формате ДД.ММ.ГГГГ: {corrected_time}")

