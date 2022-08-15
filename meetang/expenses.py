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

    return {'category': category, 'price': price, 'item': item}


def store_expense(expense):
    csv_line = expense['item'] + ',' + str(expense['price']) + ',' + expense['category']
    with open('expenses.csv', 'a+') as file_object:
        file_object.write(csv_line)


if __name__ == "__main__":
    while True:
        user_expense = input('Add your expenses: ')
        if user_expense == 'q':
            break

        expense = parse_arguments(user_expense)
        print(
            expense['category'] + ' is added to category | ' + str(
                expense['price']) + ' is added to price | ' + expense['item'] + ' is added to item')
        store_expense(expense)
