from src.decorators import log
from typing import Any


def test_log(capsys: Any) -> None:
    @log(filename="test_log.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    # Проверка корректного выполнения функции
    my_function(1, 2)
    captured = capsys.readouterr()
    assert (
            "my_function called with args: (1, 2), kwargs:{}. Result: 3\n" in captured.out
    )

    # Проверка ошибки
    try:
        my_function(0, 2)
    except TypeError:
        captured = capsys.readouterr()
        assert "my function error: " in captured.out
