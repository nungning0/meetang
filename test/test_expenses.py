from meetang import expenses


def test_arg_parsing():
    expenses.parse_arguments('vacuum bottle /workout/equip 590')
    assert expenses.price == 590
    assert expenses.item == 'vacuum bottle'
    assert expenses.category == '/workout/equip'
