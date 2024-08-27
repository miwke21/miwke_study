import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("value, result", [("1596837868705199", "1596 83** **** 5199"),
                                           ("7158300734726758", "7158 30** **** 6758"),
                                           ("8990922113665229", "8990 92** **** 5229")])
def test_get_mask_card_number(value: str, result: str) -> None:
    assert get_mask_card_number(value) == result


@pytest.mark.parametrize("values, result", [("64686473678894779589", "**9589"),
                                            ("35383033474447895560", "**5560"),
                                            ("73654108430135874305", "**4305")])
def test_get_mask_account(values: str, result: str) -> None:
    assert get_mask_account(values) == result
