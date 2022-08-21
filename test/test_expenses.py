from meetang import expenses


def test_arg_parsing():
    expense = expenses.parse_arguments('vacuum bottle /workout/equip 590')
    assert expense['price'] == 590
    assert expense['item'] == 'vacuum bottle'
    assert expense['category'] == '/workout/equip'


def test_store_load_expense():
    expense = {'category': 'workout', 'price': '590', 'item': 'vacuum bottle'}
    expenses.store_expense(expense)
    expenses_list = expenses.load_expense()
    assert expense == expenses_list[0]