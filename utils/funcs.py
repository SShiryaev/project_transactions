import json
import os


def load_transactions():
    """Фукнция чтения json файла"""
    with open(os.path.join('..', 'data', 'operations.json')) as file:
        transactions_list = json.load(file)
        return transactions_list


def format_transactions(transactions):
    """Функция форматирующая словари из json файла, возвращает словари с НЕ пустыми и
    выполненными операциями, и с НЕ пустыми данными по отправителю"""
    format_transactions_list = []
    for transaction in transactions:
        if transaction != {} and transaction['state'] == "EXECUTED" and transaction.get('from'):
            format_transactions_list.append(transaction)
    return format_transactions_list


def recent_transactions(transactions_list, len_list):
    """Функция возвращает заданное колличество словарей, отсортированных по дате"""
    sort_transactions_list = sorted(transactions_list, key=lambda x: x['date'], reverse=True)
    recent_transactions_list = sort_transactions_list[0:len_list]
    return recent_transactions_list


def recent_format_transactions(transactions, len_list):
    """Функция объединяющая функции format_transactions и recent_transactions,
    для более короткого вызова в main.py"""
    format_transactions_list = format_transactions(transactions)
    recent_transactions_list = recent_transactions(format_transactions_list, len_list)
    return recent_transactions_list


def get_correct_date(transaction):
    """Функция возвращающая дату из словаря в корректном формате"""
    num = list(transaction['date'])
    valid_num = num[8], num[9], num[7], num[5], num[6], num[4], num[0], num[1], num[2], num[3]
    valid_date = ''.join(valid_num)
    return valid_date
