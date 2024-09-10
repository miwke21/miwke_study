from unittest.mock import patch

from src.external_api import convert_to_rub


@patch("requests.get")
def test_convert_to_rub(mock_get):
    mock_get.return_value.json.return_value = '{"result": 60}'
    assert convert_to_rub(20, "USD") == 60
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=20",
        headers={"apikey": "JtLfCNxDRLiKVnZqkNZ8ET2TNVZPJLlx"},
    )