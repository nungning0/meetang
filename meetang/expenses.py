def is_price(word):
    try:
        float(word)
        return True
    except ValueError:
        return False


def parse_arguments(user_input):
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

    return category, price, item


if __name__ == "__main__":
    user_expense = input('Add your expenses: ')
    parse_arguments(user_expense)
