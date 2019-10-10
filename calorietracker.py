import warnings


def calorietracker():
    breakfastfood = []
    breakfastcalories = []

    lunchfood = []
    lunchcalories = []

    dinnerfood = []
    dinnercalories = []

    snackfood = []
    snackcalories = []

    caloriesday = int(input('How many calories would you like to limit yourself to per day?'))


    print('\nPlease list all foods consumed for breakfast and the number of calories each contains one at a time. After you have entered all breakfast items type next.')

    while True:

        food = input('Food:')

        if food == 'next':
            break

        else:

            breakfastfood.append(food)

        calories = int(input('Number of Calories:'))

        if isinstance(calories, str):
            print('\nYou must enter a number.')

        else:


            breakfastcalories.append(calories)

        breakfast = dict(zip(breakfastfood, breakfastcalories))

    print('\nYou consumed a total of {0:d} calories for breakfast.'.format(sum(breakfastcalories)))



    print('\nPlease list all foods consumed for lunch and the number of calories each contains one at a time. After you have entered all lunch items type next.')


    while True:

        food = input('Food:')

        if food == 'next':
            break

        else:

            lunchfood.append(food)

        calories = int(input('Number of Calories:'))

        if calories == 'stop':
            break

        else:

                lunchcalories.append(calories)

        lunch = dict(zip(lunchfood,lunchcalories))

    print('\nYou consumed a total of {0:d} calories for lunch.'.format(sum(lunchcalories)))



    print('\nPlease list all foods consumed for dinner and the number of calories each contains one at a time. After you have entered all dinner items type next.')

    while True:

        food = input('Food:')

        if food == 'next':
            break

        else:

            dinnerfood.append(food)

        calories = int(input('Number of Calories:'))

        if calories == 'stop':
            break

        else:

            dinnercalories.append(calories)

        dinner = dict(zip(dinnerfood, dinnercalories))

    print('\nYou consumed a total of {0:d} calories for dinner.'.format(sum(dinnercalories)))


    print('\nPlease list all snacks and desserts consumed throughout the day and the number of calories each contains one at a time. After you have entered all snacks and desserts type next.')

    while True:

        food = input('Food:')

        if food == 'next':
            break

        else:

            snackfood.append(food)

        calories = int(input('Number of Calories:'))

        if calories == 'stop':
            break

        else:

            snackcalories.append(calories)

        snack = dict(zip(snackfood, snackcalories))

    print('\nYou consumed a total of {0:d} calories for snacks.'.format(sum(snackcalories)))


    totalcalories = sum(breakfastcalories) + sum(lunchcalories) + sum(dinnercalories) + sum(snackcalories)

    print('\nYour total calorie consumption including all meals and snacks for the entire day comes to {} calories.'.format(totalcalories))

    if totalcalories > caloriesday:

        print(f'\nYou have exceeded your daily calorie limit.\n')
    else:
        print(f'\nCongratulations! You met your goal by staying under your daily calorie limit of {caloriesday} calories\n')

    from datetime import date

    foodjournal = open('foodjournal.txt', 'a+')
    foodjournal.write('\nFood Journal ' + str(date.today()))
    foodjournal.write('\n----------------BREAKFAST--------------\n')
    for key,value in breakfast.items():
        foodjournal.write(f'{key:<25} {value} calories\n')

    foodjournal.write('\n------------------LUNCH------------------\n')
    for key,value in lunch.items():
        foodjournal.write(f'{key:<25} {value} calories\n')

    foodjournal.write('\n------------------DINNER-----------------\n')
    for key,value in dinner.items():
        foodjournal.write(f'{key:<25} {value} calories\n')

    foodjournal.write('\n---------------SNACKS/DESSERTS--------------\n')
    for key, value in snack.items():
        foodjournal.write(f'{key:<25} {value} calories\n')

    foodjournal.write('\n\nTotal Calories: %d'%(totalcalories))

    if totalcalories > caloriesday:

        foodjournal.write('\nYou have exceeded your daily calorie limit.\n')
    else:
        foodjournal.write(f'\nCongratulations! You met your goal by staying under your daily calorie limit of {caloriesday} calories\n')

    foodlist = input('\nWould you like to view a list of all the foods you\'ve eaten today? Yes or no?')

    if foodlist == 'yes':

        print('\nFood Journal ' + str(date.today()),'\n')

        print('----------------BREAKFAST--------------\n')
        for key,value in breakfast.items():
            print(f'{key:<25} {value} calories')

        print('\n------------------LUNCH------------------\n')
        for key,value in lunch.items():
            print(f'{key:<25} {value} calories')

        print('\n------------------DINNER-----------------\n')
        for key,value in dinner.items():
            print(f'{key:<25} {value} calories')

        print('\n---------------SNACKS/DESSERTS--------------\n')
        for key,value in snack.items():
            print(f'{key:<25} {value} calories')

        print('\nTotal Calories: %d\n'%(totalcalories))

        if totalcalories > caloriesday:
            print(f'You have exceeded your daily calorie limit of {caloriesday} calories by {totalcalories - caloriesday} calories.')
        else:
            print(f'Congratulations! You met your goal by staying under your daily calorie limit of {caloriesday} calories. You were {caloriesday - totalcalories} calories under your limit for the day.')

    else:
        foodmonth = input('\nWould you like to view a list of your food journal for the entire month?')

        if foodmonth == 'yes':
            print(open('foodjournal.txt').read())

calorietracker()

