from pathlib import Path

import pytest

from meetang import expenses, paths
from meetang.expenses import Expense

paths.IS_TEST = True


def remove_test_expenses():
    expenses_file = Path.cwd() / "expenses.csv"
    if expenses_file.exists():
        expenses_file.unlink()


@pytest.fixture(autouse=True)
def remove_config_if_created():
    yield
    remove_test_expenses()


def test_arg_quantity_parsing():
    expense: Expense = expenses.parse_arguments('30x')
    assert expense.quantity == 30


def test_arg_parsing():
    expense: Expense = expenses.parse_arguments('vacuum bottle /workout/equip 590 3x')
    assert expense.price == 590
    assert expense.item == 'vacuum bottle'
    assert expense.category == '/workout/equip'
    assert expense.quantity == 3


def test_store_load_expense():
    expense_1 = Expense(3, 'vacuum', 600, 'workout')
    expenses.store_expense(expense_1)
    expenses_list = expenses.load_expense()
    assert expenses_list[0] == expense_1

    expense_2 = Expense(4, 'fish', 9, 'food')
    expenses.store_expense(expense_2)
    expenses_list_2 = expenses.load_expense()
    assert expenses_list_2[1] == expense_2


def max_expense(expense):
    max_value = 0
    for e in expense:
        v = e.price
    if v >= max_value:
        max_value = v

    return max_value
