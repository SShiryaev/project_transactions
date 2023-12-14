import json
import os


def load_transactions():
    with open(os.path.join('..', 'data', 'operations.json')) as file:
        transactions_list = json.load(file)
        return transactions_list
