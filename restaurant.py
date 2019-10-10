appetizers = {'Chicken Wings':8.99, 'Nachos':6.99,'Mozzarella Sticks':5.99,'Pretzels':5.99,'Onion Rings':4.99,'Cheeseburger Sliders':8.99,'Cheese Fries':8.99}
pizza = {'Cheese':{'SM':6.99,'MED':8.99,'LG':11.99},'Pepperoni':{'SM':8.99,'MED': 11.99, 'LG': 15.99},'Meat Lovers': {'SM':10.99,'MED': 13.99, 'LG': 17.99},'Supreme':{'SM':10.99,'MED': 13.99, 'LG': 17.99}}
burgers = {'Hamburger':4.99,'Cheeseburger':5.99,'Double Bacon Cheeseburger': 7.99,'Monster Burger':12.99}
sandwiches = {'Club Sandwich':7.99,'BLT':5.99,'Grilled Cheese':3.99,'Philly Cheesesteak':8.99}
desserts = {'Cheesecake':5.99,'Peanut Butter Pie':4.99,'Chocolate Mousse Cake':6.99,'Strawberry Shortcake':5.99}

order = []
item = []

ordertotal = sum(order) + (sum(order) * .043)



def mainmenu():



    print("\n\tDan's Sports Bar Menu")

    print("\t1. Appetizers")
    print("\t2. Pizza")
    print("\t3. Burgers")
    print("\t4. Sandwiches")
    print("\t5. Desserts")

    food = input('\nPlease select one of the options above to view our menu selections:')

    if food == '1' or food.casefold() == 'appetizers':
        print("\n\t\tAppetizers")
        print("\t1. Chicken Wings $8.99")
        print("\t2. Nachos $6.99")
        print("\t3. Mozzarella Sticks $5.99")
        print("\t4. Pretzels $5.99")
        print("\t5. Onion Rings $4.99")
        print("\t6. Cheeseburger Sliders $8.99")
        print("\t7. Cheese Fries $8.99")
        while True:
            appetizer = input('\nEnter the menu number to select the appetizer you would like to order. To return to the main menu type main menu.')
            if appetizer == 'main menu':
                    mainmenu()
            elif appetizer == '1':
                print('\nYou have placed an order for chicken wings.')
                order.append(float(appetizers['Chicken Wings']))
                item.append('Chicken Wings')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:

                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s,t) in zip(item,order):
                        print(f'\t{s:<30}{t}')

                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(sum(order) + (sum(order) * .043)))
                    exit()

            elif appetizer == '2':
                print('\nYou have placed an order for nachos.')
                order.append(float(appetizers['Nachos']))
                item.append('Nachos')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(sum(order) + (sum(order) * .043)))
                    exit()

            elif appetizer == '3':
                print('\nYou have placed an order for mozzarella sticks')
                order.append(float(appetizers['Mozzarella Sticks']))
                item.append('Mozzarella Sticks')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(sum(order) + (sum(order) * .043)))
                    exit()
            elif appetizer == '4':
                print('\nYou have placed an order for pretzels.')
                order.append(float(appetizers['Pretzels']))
                item.append('Pretzels')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                        sum(order) + (sum(order) * .043)))
                    exit()


            elif appetizer == '5':
                print('\nYou have placed an order for onion rings.')
                order.append(float(appetizers['Onion Rings']))
                item.append('Onion Rings')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                        sum(order) + (sum(order) * .043)))
                    exit()

            elif appetizer == '6':
                print('\nYou have placed an order for cheeseburger sliders.')
                order.append(float(appetizers['Cheeseburger Sliders']))
                item.append('Cheeseburger Sliders')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                        sum(order) + (sum(order) * .043)))
                    exit()

            elif appetizer == '7':
                print('\nYou have placed an order for cheese fries.')
                order.append(float(appetizers['Cheese Fries']))
                item.append('Cheese Fries')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                        sum(order) + (sum(order) * .043)))
                    exit()

            else:
                print('\nTo select an appetizer please enter the number beside it.')


    elif food == '2' or food.casefold() =='pizza':
        print('\n\t\tPizza')
        print('\t1.Cheese SM $6.99 MED $8.99 LG $11.99')
        print('\t2.Pepperoni SM $8.99 MED $11.99 LG $15.99')
        print('\t3.Meat Lovers SM $10.99 MED $13.99 LG $17.99')
        print('\t4.Supreme SM $10.99 MED $13.99 LG $17.99')

        while True:
            pizzas = input('\nEnter the menu number to select the pizza you would like to order. To return to the main menu type main menu.')
            if pizzas == 'main menu':
                mainmenu()
            elif pizzas == '1':
                print('\nYou have placed an order for cheese pizza.')
                while True:

                    size = input('\nWhat size pizza would you like to order? Type small, medium, or large.')

                    if size.casefold() == 'small':
                        order.append(float(pizza['Cheese']['SM']))
                        item.append('SM Cheese Pizza')
                        checkout = input('Would you like to order another item on the menu? Type yes or no.')

                        if checkout == 'yes' or checkout == 'y':
                            mainmenu()
                        else:
                            print('\n\tDan\'s Sports Bar Menu Receipt')
                            print('\t------------------------------\n')
                            for (s, t) in zip(item, order):
                                print(f'\t{s:<30}{t}')
                            print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                                sum(order) + (sum(order) * .043)))
                            exit()
                    if size.casefold() == 'medium':
                        order.append(float(pizza['Cheese']['MED']))
                        item.append('MED Cheese Pizza')
                        checkout = input('Would you like to order another item on the menu? Type yes or no.')

                        if checkout == 'yes' or checkout == 'y':
                            mainmenu()
                        else:
                            print('\n\tDan\'s Sports Bar Menu Receipt')
                            print('\t------------------------------\n')
                            for (s, t) in zip(item, order):
                                print(f'\t{s:<30}{t}')
                            print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                                sum(order) + (sum(order) * .043)))
                            exit()
                    if size.casefold() == 'large':
                        order.append(float(pizza['Cheese']['LG']))
                        item.append('LG Cheese Pizza')
                        checkout = input('Would you like to order another item on the menu? Type yes or no.')

                        if checkout == 'yes' or checkout == 'y':
                            mainmenu()
                        else:
                            print('\n\tDan\'s Sports Bar Menu Receipt')
                            print('\t------------------------------\n')
                            for (s, t) in zip(item, order):
                                print(f'\t{s:<30}{t}')
                            print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                                sum(order) + (sum(order) * .043)))
                            exit()
                    else: print('\nPlease type small,medium, or large to choose which size pizza you want.')
            elif pizzas == '2':
                print('\nYou have placed an order for pepperoni pizza.')
                while True:

                    size = input('\nWhat size pizza would you like to order? Type small, medium, or large.')

                    if size.casefold() == 'small':
                        order.append(float(pizza['Pepperoni']['SM']))
                        item.append('SM Pepperoni Pizza')
                        checkout = input('Would you like to order another item on the menu? Type yes or no.')

                        if checkout == 'yes' or checkout == 'y':
                            mainmenu()
                        else:
                            print('\n\tDan\'s Sports Bar Menu Receipt')
                            print('\t------------------------------\n')
                            for (s, t) in zip(item, order):
                                print(f'\t{s:<30}{t}')
                            print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                                sum(order) + (sum(order) * .043)))
                            exit()
                    if size.casefold() == 'medium':
                        order.append(float(pizza['Pepperoni']['MED']))
                        item.append('MED Pepperoni Pizza')
                        checkout = input('Would you like to order another item on the menu? Type yes or no.')

                        if checkout == 'yes' or checkout == 'y':
                            mainmenu()
                        else:
                            print('\n\tDan\'s Sports Bar Menu Receipt')
                            print('\t------------------------------\n')
                            for (s, t) in zip(item, order):
                                print(f'\t{s:<30}{t}')
                            print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                                sum(order) + (sum(order) * .043)))
                            exit()
                    if size.casefold() == 'large':
                        order.append(float(pizza['Pepperoni']['LG']))
                        item.append('LG Pepperoni Pizza')
                        checkout = input('Would you like to order another item on the menu? Type yes or no.')

                        if checkout == 'yes' or checkout == 'y':
                            mainmenu()
                        else:
                            print('\n\tDan\'s Sports Bar Menu Receipt')
                            print('\t------------------------------\n')
                            for (s, t) in zip(item, order):
                                print(f'\t{s:<30}{t}')
                            print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                                sum(order) + (sum(order) * .043)))
                            exit()
                    else: print('\nPlease type small,medium, or large to choose which size pizza you want.')
            elif pizzas == '3':
                print('\nYou have placed an order for a Meat Lovers Pizza.')
                while True:

                    size = input('\nWhat size pizza would you like to order? Type small, medium, or large.')

                    if size.casefold() == 'small':
                        order.append(float(pizza['Meat Lovers']['SM']))
                        item.append('SM Meat Lovers Pizza')
                        checkout = input('Would you like to order another item on the menu? Type yes or no.')

                        if checkout == 'yes' or checkout == 'y':
                            mainmenu()
                        else:
                            print('\n\tDan\'s Sports Bar Menu Receipt')
                            print('\t------------------------------\n')
                            for (s, t) in zip(item, order):
                                print(f'\t{s:<30}{t}')
                            print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                                sum(order) + (sum(order) * .043)))
                            exit()
                    if size.casefold() == 'medium':
                        order.append(float(pizza['Meat Lovers']['MED']))
                        item.append('MED Meat Lovers Pizza')
                        checkout = input('Would you like to order another item on the menu? Type yes or no.')

                        if checkout == 'yes' or checkout == 'y':
                            mainmenu()
                        else:
                            print('\n\tDan\'s Sports Bar Menu Receipt')
                            print('\t------------------------------\n')
                            for (s, t) in zip(item, order):
                                print(f'\t{s:<30}{t}')
                            print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                                sum(order) + (sum(order) * .043)))
                            exit()
                    if size.casefold() == 'large':
                        order.append(float(pizza['Meat Lovers']['LG']))
                        item.append('LG Meat Lovers Pizza')
                        checkout = input('Would you like to order another item on the menu? Type yes or no.')

                        if checkout == 'yes' or checkout == 'y':
                            mainmenu()
                        else:
                            print('\n\tDan\'s Sports Bar Menu Receipt')
                            print('\t------------------------------\n')
                            for (s, t) in zip(item, order):
                                print(f'\t{s:<30}{t}')
                            print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                                sum(order) + (sum(order) * .043)))
                            exit()
                    else: print('\nPlease type small,medium, or large to choose which size pizza you want.')
            elif pizzas == '4':
                print('\nYou have placed an order for a Supreme Pizza.')
                while True:

                    size = input('\nWhat size pizza would you like to order? Type small, medium, or large.')

                    if size.casefold() == 'small':
                        order.append(float(pizza['Supreme']['SM']))
                        item.append('SM Supreme Pizza')
                        checkout = input('Would you like to order another item on the menu? Type yes or no.')

                        if checkout == 'yes' or checkout == 'y':
                            mainmenu()
                        else:
                            print('\n\tDan\'s Sports Bar Menu Receipt')
                            print('\t------------------------------\n')
                            for (s, t) in zip(item, order):
                                print(f'\t{s:<30}{t}')
                            print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                                sum(order) + (sum(order) * .043)))
                            exit()
                    if size.casefold() == 'medium':
                        order.append(float(pizza['Supreme']['MED']))
                        item.append('MED Supreme Pizza')
                        checkout = input('Would you like to order another item on the menu? Type yes or no.')

                        if checkout == 'yes' or checkout == 'y':
                            mainmenu()
                        else:
                            print('\n\tDan\'s Sports Bar Menu Receipt')
                            print('\t------------------------------\n')
                            for (s, t) in zip(item, order):
                                print(f'\t{s:<30}{t}')
                            print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                                sum(order) + (sum(order) * .043)))
                            exit()
                    if size.casefold() == 'large':
                        order.append(float(pizza['Supreme']['LG']))
                        item.append('LG Supreme Pizza')
                        checkout = input('Would you like to order another item on the menu? Type yes or no.')

                        if checkout == 'yes' or checkout == 'y':
                            mainmenu()
                        else:
                            print('\n\tDan\'s Sports Bar Menu Receipt')
                            print('\t------------------------------\n')
                            for (s, t) in zip(item, order):
                                print(f'\t{s:<30}{t}')
                            print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                                sum(order) + (sum(order) * .043)))
                            exit()
                    else: print('\nPlease type small,medium, or large to choose which size pizza you want.')
            else:
                print('\nTo select a pizza please enter the number beside it.')
    elif food == '3' or food.casefold() == 'burgers':
        print('\n\t\tBurgers')
        print('\t1. Hamburger $4.99')
        print('\t2. Cheeseburger $5.99')
        print('\t3. Double Bacon Cheeseburger $7.99')
        print('\t4. Monster Burger $12.99')
        while True:
            burger = input('\nEnter the menu number to select the burger you would like to order. To return to the main menu type main menu.')
            if burger == 'main menu':
                    mainmenu()
            elif burger == '1':
                print('\nYou have placed an order for a hamburger.')
                order.append(float(burgers['Hamburger']))
                item.append('Hamburger')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                        sum(order) + (sum(order) * .043)))
                    exit()
            elif burger == '2':
                print('\nYou have placed on order for a cheeseburger.')
                order.append(float(burgers['Cheeseburger']))
                item.append('Cheeseburger')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                        sum(order) + (sum(order) * .043)))
                    exit()
            elif burger == '3':
                print('\nYou have placed on order for a double bacon cheeseburger.')
                order.append(float(burgers['Double Bacon Cheeseburger']))
                item.append('Double Bacon Cheeseburger')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                        sum(order) + (sum(order) * .043)))
                    exit()
            elif burger == '4':
                print('\nYou have placed on order for a monster burger.')
                order.append(float(burgers['Monster Burger']))
                item.append('Monster Burger')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                        sum(order) + (sum(order) * .043)))
                    exit()
            else:
                print('\nTo select a burger please enter the number beside it.')

    elif food == '4' or food.casefold() == 'sandwiches':
        print('\n\t\tSandwiches')
        print('\t1. Club Sandwich $7.99')
        print('\t2. BLT $5.99')
        print('\t3. Grilled Cheese $3.99')
        print('\t4. Philly Cheesesteak $8.99')
        while True:
            sandwich = input('\nEnter the menu number to select the sandwich you would like to order. To return to the main menu type main menu.')
            if sandwich == 'main menu':
                    mainmenu()
            elif sandwich == '1':
                print('\nYou have placed an order for a club sandwich.')
                order.append(float(sandwiches['Club Sandwich']))
                item.append('Club Sandwich')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                        sum(order) + (sum(order) * .043)))
                    exit()

            elif sandwich == '2':
                print('\nYou have placed an order for a BLT.')
                order.append(float(sandwiches['BLT']))
                item.append('BLT')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                        sum(order) + (sum(order) * .043)))
                    exit()

            elif sandwich == '3':
                print('\nYou have placed an order for a grilled cheese.')
                order.append(float(sandwiches['Grilled Cheese']))
                item.append('Grilled Cheese')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                        sum(order) + (sum(order) * .043)))
                    exit()

            elif sandwich == '4':
                print('\nYou have placed an order for a philly cheesesteak.')
                order.append(float(sandwiches['Philly Cheesesteak']))
                item.append('Philly Cheesesteak')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                        sum(order) + (sum(order) * .043)))
                    exit()

            else:
                print('\nTo select a sandwich please enter the number beside it.')

    elif food == '5' or food.casefold() == 'desserts':
        print('\n\t\tDesserts')
        print('\t1.Cheesecake $5.99')
        print('\t2.Peanut Butter Pie $4.99')
        print('\t3.Chocolate Mousse Cake $6.99')
        print('\t4.Strawberry Shortcake $5.99')
        while True:
            dessert = input('\nEnter the menu number to select the dessert you would like to order. To return to the main menu type main menu.')
            if dessert == 'main menu':
                    mainmenu()
            elif dessert == '1':
                print('\nYou have placed an order for cheesecake.')
                order.append(float(desserts['Cheesecake']))
                item.append('Cheesecake')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                        sum(order) + (sum(order) * .043)))
                    exit()
            elif dessert == '2':
                print('\nYou have placed an order for Peanut Butter Pie.')
                order.append(float(desserts['Peanut Butter Pie']))
                item.append('Peanut Butter Pie')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                        sum(order) + (sum(order) * .043)))
                    exit()
            elif dessert == '3':
                print('\nYou have placed an order for Chocolate Mousse Cake.')
                order.append(float(desserts['Chocolate Mousse Cake']))
                item.append('Chocolate Mousse Cake')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                        sum(order) + (sum(order) * .043)))
                    exit()
            elif dessert == '4':
                print('\nYou have placed an order for Strawberry Shortcake.')
                order.append(float(desserts['Strawberry Shortcake']))
                item.append('Strawberry Shortcake')
                checkout = input('Would you like to order another item on the menu? Type yes or no.')

                if checkout == 'yes' or checkout == 'y':
                    mainmenu()
                else:
                    print('\n\tDan\'s Sports Bar Menu Receipt')
                    print('\t------------------------------\n')
                    for (s, t) in zip(item, order):
                        print(f'\t{s:<30}{t}')
                    print('\nThe total for your order comes to ${0:.2f} including tax. Have a nice day!'.format(
                        sum(order) + (sum(order) * .043)))
                    exit()
            else:
                print('\nTo select a dessert please enter the number beside it.')
    else:print('\nYou must select by choosing the corresponding number. Please type 1,2,3,4, or 5')
    mainmenu()

mainmenu()


