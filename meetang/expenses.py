user_expense = input('Add your expenses: ')

item = ''
category = ''
price = -1

args = user_expense.split()


def is_price(word):
    try:
        float(word)
        return True
    except ValueError:
        return False


for arg in args:
    if arg.startswith('/'):
        category = arg
    elif is_price(arg):
        price = float(arg)

print("This is category: " + category)
print("This is price: " + str(price))
