from utils.funcs import load_transactions, recent_format_transactions, user_form_transactions

data = load_transactions()
user_form = recent_format_transactions(data, 5)
user_interface = user_form_transactions(user_form)
