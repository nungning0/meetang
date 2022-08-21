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


def load_expense():
    expenses = []

    with open('expenses.csv') as file_object:
        lines = file_object.readlines()
        for line in lines:
            item, price, category, *_ = line.split(',')
            expense = {'category': category, 'price': price, 'item': item}
            expenses.append(expense)

    return expenses


if __name__ == "__main__":
    while True:
        user_input = input('Add your expenses: ')
        if user_input == 'q':
            break

        parsed_expense = parse_arguments(user_input)
        print(
            parsed_expense['category'] + ' is added to category | ' + str(
                parsed_expense['price']) + ' is added to price | ' + parsed_expense['item'] + ' is added to item')
        store_expense(parsed_expense)
