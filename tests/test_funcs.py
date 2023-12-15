from utils.funcs import (format_transactions, recent_transactions, recent_format_transactions,
                         correct_date, correct_card_number, correct_bank_account)


def test_format_transactions(fixture_list_array, fixture_valid_array_format):
    assert format_transactions(fixture_list_array) == fixture_valid_array_format


def test_recent_transactions(fixture_valid_array_format, fixture_valid_array_recent):
    assert recent_transactions(fixture_valid_array_format, 9) == fixture_valid_array_recent
    assert recent_transactions(fixture_valid_array_format, 0) == fixture_valid_array_recent[:0]


def test_recent_format_transactions(fixture_valid_array_format, fixture_valid_array_recent):
    assert recent_format_transactions(fixture_valid_array_format, 7) == fixture_valid_array_recent[:7]
    assert recent_format_transactions(fixture_valid_array_format, 5) == fixture_valid_array_recent[:5]


def test_correct_date():
    assert correct_date('2019-12-07') == '07-12-2019'
    assert correct_date('2015-03-25') == '25-03-2015'


def test_correct_card_number():
    assert correct_card_number('0123456789012345') == '0123 45** **** 2345'
    assert correct_card_number('2842871234569012') == '2842 87** **** 9012'


def test_correct_bank_account():
    assert correct_bank_account('72731966109147704472') == '**4472'
    assert correct_bank_account('11776614605963066702') == '**6702'
