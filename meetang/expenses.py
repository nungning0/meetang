from dataclasses import dataclass
from typing import List


@dataclass
class Expense:
    item: str
    price: float
    category: str


def expense_i(inf):
    print(f"this is {inf.item} cost {inf.price} category {inf.category}")


v = Expense('fish', 900, 'food')
expense_i(v)


def is_price(word):
    try:
        float(word)
        return True
    except ValueError:
        return False


def parse_arguments(user_input) -> Expense:
    item = ''
    category = ''
    price = -1

    args = user_input.split()
    for arg in args:
        if arg.startswith('/'):
            category = arg
        elif is_price(arg):
            price = float(arg)
        else:
            item = item.lstrip()
            item += " " + arg

    return Expense(item, price, category)


def store_expense(expense: Expense):
    csv_line = expense.item + ',' + str(expense.price) + ',' + expense.category + '\n'
    with open('expenses.csv', 'a+') as file_object:
        file_object.write(csv_line)


def load_expense() -> List[Expense]:
    expenses : List[Expense] = []

    with open('expenses.csv') as file_object:
        lines = file_object.readlines()
        for line in lines:
            item, price, category, *_ = line.rstrip().split(',')
            expense = Expense(item, float(price), category)
            expenses.append(expense)

    return expenses


if __name__ == "__main__":
    while True:
        user_input = input('Add your expenses: ')
        if user_input == 'q':
            break

        parsed_expense : Expense = parse_arguments(user_input)
        print(
            f"""{parsed_expense.item} is added to item 
                {parsed_expense.price} is added to price {parsed_expense.category} is added to category)""")
        store_expense(parsed_expense)
