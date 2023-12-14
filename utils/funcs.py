import json
import os


def load_transactions():
    with open(os.path.join('..', 'data', 'operations.json')) as file:
        transactions_list = json.load(file)
        return transactions_list


def format_transactions(transactions):
    format_transactions_list = []
    for transaction in transactions:
        if transaction != {} and transaction['state'] == "EXECUTED":
            format_transactions_list.append(transaction)
    return format_transactions_list
