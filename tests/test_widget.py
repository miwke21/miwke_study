import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def card_or_account_info() -> str:
    return "Maestro 2345234545674567"


@pytest.fixture
def date_info() -> str:
    return "2018-07-11T02:26:18.671407"


def test_mask_account_card(card_or_account_info: str) -> None:
    assert mask_account_card(card_or_account_info) == "Maestro 2345 23** **** 4567"


def test_get_date(date_info: str) -> None:
    assert get_date(date_info) == "11.07.2018"
