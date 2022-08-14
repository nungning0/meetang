item = ''
category = ''
price = -1


def is_price(word):
    try:
        float(word)
        return True
    except ValueError:
        return False


def parse_arguments(user_input):
    global category, price, item
    args = user_input.split()
    for arg in args:
        if arg.startswith('/'):
            category = arg
        elif is_price(arg):
            price = float(arg)
        else:
            item = item.lstrip()
            item += " " + arg


if __name__ == "__main__":
    user_expense = input('Add your expenses: ')
    parse_arguments(user_expense)

print("This is category: " + category)
print("This is price: " + str(price))
print("This is item: " + item)
