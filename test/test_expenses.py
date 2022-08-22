from pathlib import Path

import pytest

from meetang import expenses
from meetang.expenses import Expense


def remove_test_expenses():
    expenses_file = Path.cwd() / "expenses.csv"
    if expenses_file.exists():
        expenses_file.unlink()


@pytest.fixture(autouse=True)
def remove_config_if_created():
    yield
    remove_test_expenses()


def test_arg_parsing():
    expense: Expense = expenses.parse_arguments('vacuum bottle /workout/equip 590')
    assert expense.price == 590
    assert expense.item == 'vacuum bottle'
    assert expense.category == '/workout/equip'


def test_store_load_expense():
    expense_1 = Expense('vacuum', 600, 'workout')
    expenses.store_expense(expense_1)
    expenses_list = expenses.load_expense()
    assert expense_1 == expenses_list[0]

    expense_2 = Expense('fish', 9, 'food')
    expenses.store_expense(expense_2)
    expenses_list_2 = expenses.load_expense()
    assert expense_2 == expenses_list_2[1]
