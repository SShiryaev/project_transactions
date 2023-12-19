from utils.funcs import (load_transactions, recent_format_transactions,
                         correct_date, correct_bank_account, correct_card_number)


def user_form_transactions():
    data = load_transactions()
    user_form = recent_format_transactions(data, 5)
    for transaction in user_form:
        valid_date = correct_date(transaction['date'])
        discription = transaction['description']
        if 'Счет' in transaction['from']:
            from_where = correct_bank_account(transaction['from'])
        else:
            from_where = correct_card_number(transaction['from'])
        to_where = correct_bank_account(transaction['to'])
        amount = transaction['operationAmount']['amount']
        currency = transaction['operationAmount']['currency']['name']
        print(f'\n{valid_date} {discription}\n{from_where} -> {to_where}\n{amount} {currency}')


user_form_transactions()
