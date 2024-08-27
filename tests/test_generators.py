from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def test_transaction_descriptions() -> None:
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_card_number_generator() -> None:
    generator = card_number_generator(1, 4)
    assert (next(generator)) == "0000 0000 0000 0001"
    assert (next(generator)) == "0000 0000 0000 0002"
    assert (next(generator)) == "0000 0000 0000 0003"
    assert (next(generator)) == "0000 0000 0000 0004"


def test_filter_by_currency():
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == {'date': '2018-06-30T02:08:58.425572',
 'description': 'Перевод организации',
 'from': 'Счет 75106830613657916952',
 'id': 939719570,
 'operationAmount': {'amount': '9824.07',
                     'currency': {'code': 'USD', 'name': 'USD'}},
 'state': 'EXECUTED',
 'to': 'Счет 11776614605963066702'}
    assert next(generator) == {'date': '2019-04-04T23:20:05.206878',
 'description': 'Перевод со счета на счет',
 'from': 'Счет 19708645243227258542',
 'id': 142264268,
 'operationAmount': {'amount': '79114.93',
                     'currency': {'code': 'USD', 'name': 'USD'}},
 'state': 'EXECUTED',
 'to': 'Счет 75651667383060284188'}
    assert next(generator) == {'date': '2018-08-19T04:27:37.904916',
 'description': 'Перевод с карты на карту',
 'from': 'Visa Classic 6831982476737658',
 'id': 895315941,
 'operationAmount': {'amount': '56883.54',
                     'currency': {'code': 'USD', 'name': 'USD'}},
 'state': 'EXECUTED',
 'to': 'Visa Platinum 8990922113665229'}
    generator_1 = filter_by_currency(transactions, "RUB")
    assert next(generator_1) == {'date': '2019-03-23T01:09:46.296404',
 'description': 'Перевод со счета на счет',
 'from': 'Счет 44812258784861134719',
 'id': 873106923,
 'operationAmount': {'amount': '43318.34',
                     'currency': {'code': 'RUB', 'name': 'руб.'}},
 'state': 'EXECUTED',
 'to': 'Счет 74489636417521191160'}
    assert next(generator_1) == {'date': '2018-09-12T21:27:25.241689',
 'description': 'Перевод организации',
 'from': 'Visa Platinum 1246377376343588',
 'id': 594226727,
 'operationAmount': {'amount': '67314.70',
                     'currency': {'code': 'RUB', 'name': 'руб.'}},
 'state': 'CANCELED',
 'to': 'Счет 14211924144426031657'}
