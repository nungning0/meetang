import datetime
import re
from dataclasses import dataclass
from datetime import timedelta
from typing import List, Iterable, Optional

from meetang import paths

quantity_regex = re.compile(r'^\d+x|X$')
price_regex = re.compile(r'\d*[.,]?\d*')


@dataclass
class Expense:
    quantity: int
    item: str
    price: float
    category: str
    date: datetime.date = datetime.date.today()

    def is_valid(self) -> bool:
        return self.quantity > 0 and self.price >= 0 and (bool(self.item) or bool(self.category))

    def __str__(self):
        return f'{self.quantity}x {self.item} for {self.price} in {self.category} on {self.date}'


class InvalidInput(Exception):
    pass


def parse_arguments(user_input: str) -> Expense:
    """
    :param user_input: terminal input representing single expense
    :return: instance of Expense
    """
    item = ''
    category = ''
    price = 0
    quantity = 1
    date = datetime.date.today()

    args: List[str] = user_input.split()
    for arg in args:
        if arg.startswith('/'):
            category = arg
        elif quantity_regex.fullmatch(arg):
            quantity = int(arg[:-1])
        elif price_regex.fullmatch(arg):
            price = float(arg)
        elif arg == 'yesterday':
            date = datetime.date.today() - timedelta(days=1)
        else:
            item += arg + " "

    return Expense(quantity, item.rstrip(), price, category, date)


def store_expense(expense: Expense):
    csv_line = str(expense.date) + ',' + str(expense.quantity) + ',' + expense.item + ',' + str(expense.price) + ',' + expense.category + '\n'
    with open(paths.expenses_path(True), 'a+') as file_object:
        file_object.write(csv_line)


def load_expense() -> List[Expense]:
    expenses: List[Expense] = []

    with open(paths.expenses_path()) as file_object:
        lines = file_object.readlines()
        for line in lines:
            date, quantity, item, price, category, *_ = line.rstrip().split(',')
            dt_object = datetime.date.fromisoformat(date)
            expense = Expense(int(quantity), item, float(price), category, dt_object)
            expenses.append(expense)

    return expenses


def print_expenses_table(expenses: List[Expense]):
    padding = 30
    price_padding = 10
    print(f"|quantity{' ' * (padding - 2)}| Item{' ' * (padding - 4)}| Price{' ' * (price_padding - 5)}| Category{' ' * (padding - 8)}")
    print("-" * (padding * 3 + 17))
    for expense in expenses:
        print(
            f"| {expense.quantity}{' ' * (padding - len(str(expense.quantity)))}|{expense.item}{' ' * (padding - len(expense.item))}| {expense.price}{' ' * (price_padding - len(str(expense.price)))}| {expense.category}{' ' * (padding - len(expense.category))}")

    print(f"Total: {calc_sum(expenses)}")
    print(f"Highest Expense: {max_expense(expenses)}")


def calc_sum(expenses: Iterable[Expense]) -> float:
    return sum([expense.price for expense in expenses])


def max_expense(expenses: List[Expense]) -> Optional[Expense]:
    sorted_expenses = sorted(expenses, key=lambda e: e.price, reverse=True)
    if not expenses:
        return None

    return sorted_expenses[0]


if __name__ == "__main__":
    while True:
        user_input: str = input('Add your expenses: ')
        parsed_expense: Expense = parse_arguments(user_input)

        if not parsed_expense.is_valid():
            print("Invalid input: at least one of item or category is mandatory")
            continue

        print(parsed_expense)
        store_expense(parsed_expense)
