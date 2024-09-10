import json
import logging
from typing import Any

from src.external_api import convert_to_rub

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/utils.log",
    filemode="w",
)

logger = logging.getLogger("utils")


def get_transactions_dictionary(path: str) -> Any:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger.info("Getting transaction list starts")
        with open(path, "r", encoding="utf-8") as operations:
            try:
                transactions_data = json.load(operations)
                logger.info("Transactions list ready")
                return transactions_data
            except json.JSONDecodeError:
                logger.error("Decode error")
                transactions_data = []
                return transactions_data
    except FileNotFoundError:
        logger.error("File was not found")
        transactions_data = []
        return transactions_data


def return_transaction_amount_in_rub(transactions: list, transaction_id: int) -> Any:
    """Функция принимает транзакцию и возвращает сумму транзакции в рублях, если не в рублях, конвертирует в рубли"""
    logger.info("Getting operation amount starts")
    for transaction in transactions:
        if transaction.get("id") == transaction_id:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                rub_amount = transaction["operationAmount"]["amount"]
                logger.info(f"Operation amount in RUB:{rub_amount}")
                return rub_amount
            else:
                not_rub_amount = transaction["operationAmount"]["amount"]
                logger.info(f"Operation amount in USD/EUR:{not_rub_amount}")
                currency = transaction["operationAmount"]["currency"]["code"]
                rub_amount = round(convert_to_rub(not_rub_amount, currency), 2)
                if rub_amount != 0:
                    logger.info(f"Operation amount in RUB:{rub_amount}")
                    return rub_amount
                else:
                    logger.error("Operation amount can't be converted to RUB")
                    return "Конвертация не может быть выполнена"
    else:
        logger.error("Transaction not found")
        return "Транзакция не найдена"


if __name__ == "__main__":
    transactions = get_transactions_dictionary("../data/operations.json")
    print(return_transaction_amount_in_rub(transactions, 41428829))
