from datetime import datetime


def filter_by_state(data, state='EXECUTED'):
    """
    Сортировка списка по ключу 'EXECUTED'.

    :param data: Данные для сортировки.
    :param state: Определение ключа для сортировки.
    :return: Отсортированный список с данным ключом.
    """
    return [entry for entry in data if entry.get('state') == state]


def sort_by_date(data, reverse=True):
    """
    Сортирует список словарей по дате по убыванию.

    :param data: Список для сортировки.
    :param reverse: Определение порядка по убывающей.
    :return: Отсортированный список.
    """
    return sorted(data, key=lambda x: datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse)

# Примеры входных данных для проверки функции
data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


filtered_data = filter_by_state(data)
print(filtered_data)


sorted_data = sort_by_date(data)
print(sorted_data)
