import json
import os


def load_transactions():
    """Фукнция чтения json файла"""
    with open(os.path.join('data', 'operations.json'), encoding='utf-8') as file:
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


def correct_date(date):
    """Функция возвращающая дату из словаря в корректном формате"""
    list_date = list(date)
    list_date[7] = '.'
    list_date[4] = '.'
    valid_num = (list_date[8], list_date[9], list_date[7], list_date[5], list_date[6],
                 list_date[4], list_date[0], list_date[1], list_date[2], list_date[3])
    valid_date = ''.join(valid_num)
    return valid_date


def correct_card_number(from_or_to):
    """Функция возвращает замаскированный и разбитый по 4 символа номер карты"""
    list_from_where = from_or_to.split()
    card_number = list_from_where[-1]
    valid_card_number = card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[12:]
    list_from_where[-1] = valid_card_number
    valid_card_number_from_or_to = ' '.join(list_from_where)
    return valid_card_number_from_or_to


def correct_bank_account(from_or_to):
    """Функция возвращает замаскированный и не отображающийся целиком
    номер счета"""
    list_from_or_to = from_or_to.split()
    bank_account = list_from_or_to[-1]
    valid_bank_account = '**' + bank_account[16:]
    list_from_or_to[-1] = valid_bank_account
    valid_bank_account_from_or_to = ' '.join(list_from_or_to)
    return valid_bank_account_from_or_to
