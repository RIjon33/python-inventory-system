while(True):
    print('''
    ---------------------------------------
            !!!INVENTORY SYSTEM!!!
    ---------------------------------------
    1 = View Items
    2 = Add Items
    3 = Exit''')

    choice = int(input('Enter Your Answer =  '))
    if choice == 1:
        print('------------------')
        print('Items:')
        data = open("inventory.txt", "r")
        items = data.readlines()
        for item in items:
            print(item)
        print('------------------')
    elif choice == 2:
        print('------------------')
        print('Add Items:')
        print('------------------')
        thing = str(input("Add Item: "))
        append = open("Inventory.txt", "a")
        append.write(',' + thing)
        append.close()
    elif choice == 3:
        print('Have a good day!')
        break
    else:
        break
