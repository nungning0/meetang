from meetang import expenses


def test_arg_parsing():
    expense = expenses.parse_arguments('vacuum bottle /workout/equip 590')
    assert expense['price'] == 590
    assert expense['item'] == 'vacuum bottle'
    assert expense['category'] == '/workout/equip'
