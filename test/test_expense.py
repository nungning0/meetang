from meetang.expenses import Expense


def test_is_valid():
    assert Expense(3, 'vacuum', 600, '/workout').is_valid() is True
    assert Expense(3, 'vacuum', 600, '').is_valid() is True
    assert Expense(3, '', 600, '/workout').is_valid() is True
    assert Expense(3, '', 600, '').is_valid() is False
    assert Expense(0, 'vacuum', 600, '/workout').is_valid() is False
    assert Expense(1, 'vacuum', -100, '/workout').is_valid() is False
    assert Expense(0, 'vacuum', -100, '/workout').is_valid() is False
    assert Expense(1, 'vacuum', 600, 'workout').is_valid() is True
    assert Expense(0, '', -100, '').is_valid() is False


