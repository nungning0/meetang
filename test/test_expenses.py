from meetang import expenses


def test_arg_parsing():
    result = expenses.parse_arguments('vacuum bottle /workout/equip 590')
    assert result['price'] == 590
    assert result['item'] == 'vacuum bottle'
    assert result['category'] == '/workout/equip'
