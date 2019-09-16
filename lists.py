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