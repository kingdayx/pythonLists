shopping_list = []


def add_to_list(item):
    shopping_list.append(item)
    print("The item was added! There are now {} items in the list!".format(len(shopping_list)))


def show_help():
    print("""
    Enter 'DONE' to finish adding items
    Enter 'HELP' to bring up help
    """)


show_help()
while True:
    new_item = input("> ")
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    # call add_to_list with new_item as argument
    add_to_list(new_item)

