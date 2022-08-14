from meetang import expenses


def test_arg_parsing():
    result = expenses.parse_arguments('vacuum bottle /workout/equip 590')
    assert result[1] == 590
    assert result[2] == 'vacuum bottle'
    assert result[0] == '/workout/equip'
