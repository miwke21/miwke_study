from typing import Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


# Фикстура для предоставления данных для тестов
@pytest.fixture
def sample_data() -> List[Dict]:
    data: List[Dict] = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    return data


# Тест для функции filter_by_state
def test_filter_by_state(sample_data: List[Dict]) -> None:
    filtered_data = filter_by_state(sample_data)
    for entry in filtered_data:
        assert entry.get('state') == 'EXECUTED'


# Тест для функции sort_by_date
@pytest.mark.parametrize("reverse", [True, False])
def test_sort_by_date(sample_data: List[Dict], reverse: bool) -> None:
    sorted_data = sort_by_date(sample_data, reverse)
    dates = [entry['date'] for entry in sorted_data]
    sorted_dates = sorted(dates, reverse=reverse)
    assert dates == sorted_dates
