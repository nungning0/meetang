from dataclasses import dataclass
from typing import List, Iterable, Optional

from meetang import paths


@dataclass
class Expense:
    item: str
    price: float
    category: str

    def __str__(self):
        return f'{self.item} for {self.price} in {self.category}'


def is_price(word):
    try:
        float(word)
        return True
    except ValueError:
        return False


def parse_arguments(user_input: str) -> Expense:
    item = ''
    category = ''
    price = -1

    args: List[str] = user_input.split()
    for arg in args:
        if arg.startswith('/'):
            category = arg
        elif is_price(arg):
            price = float(arg)
        else:
            item += arg + " "

    return Expense(item.rstrip(), price, category)


def store_expense(expense: Expense):
    csv_line = expense.item + ',' + str(expense.price) + ',' + expense.category + '\n'
    with open(paths.expenses_path(True), 'a+') as file_object:
        file_object.write(csv_line)


def load_expense() -> List[Expense]:
    expenses: List[Expense] = []

    with open(paths.expenses_path()) as file_object:
        lines = file_object.readlines()
        for line in lines:
            item, price, category, *_ = line.rstrip().split(',')
            expense = Expense(item, float(price), category)
            expenses.append(expense)

    return expenses


def print_expenses_table(expenses: List[Expense]):
    padding = 30
    price_padding = 10
    print(f"| Item{' ' * (padding - 4)}| Price{' ' * (price_padding - 5)}| Category{' ' * (padding - 8)}")
    print("-" * (padding * 3 + 17))
    for expense in expenses:
        print(
            f"| {expense.item}{' ' * (padding - len(expense.item))}| {expense.price}{' ' * (price_padding - len(str(expense.price)))}| {expense.category}{' ' * (padding - len(expense.category))}")

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
    prompt = ("What would you like to do? Enter one of the option:\n"
              "a) Add expense\n"
              "p) Print expenses\n"
              "q) Quit\n"
              "Command: ")
    while True:
        user_cmd = input(prompt).strip()
        if user_cmd == 'q':
            break
        if user_cmd == 'a':
            while True:
                user_input: str = input('Add your expenses: ')
                parsed_expense: Expense = parse_arguments(user_input)
                if not parsed_expense.item:
                    print("no item")
                else:
                    print(parsed_expense)
                    store_expense(parsed_expense)
                    break
        elif user_cmd == 'p':
            print_expenses_table(load_expense())
            print()
