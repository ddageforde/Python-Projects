

savingsbal = [20000]
checkingbal = [2000]

def mainmenu():

    global checkingbal
    global savingsbal



    print("\n\tWelcome to Bank of America!")


    print("\n\t\tMain Menu")
    print("\t1. Deposit")
    print("\t2. Withdrawal")
    print("\t3. Transfer")
    print("\t4. Balance Inquiry")

    bank = input('\nPlease select one of the options above:')

    if bank == '1' or bank.casefold() == 'deposit':
        while True:
            typedeposit = input('Would you like to make a deposit in your checking or savings account?')

            if typedeposit == 'checking':
                while True:
                    checking = input('How much money would you like to deposit into your checking account?')

                    if checking.isnumeric():

                        print('\n${0:.2f} has been added into your checking account.'.format(float(checking)))
                        checkingbal.append(float(checking))
                        atransaction = input('Would you like to make another transaction? Yes or no?')

                        if atransaction == "yes" or atransaction == "y":
                            mainmenu()
                        else:
                            print('\nThank you for choosing Bank of America! Have a nice day!')
                        exit()

                    else:print('You must enter a number.')


            elif typedeposit == 'savings':
                while True:
                    savings = input('How much money would you like to deposit into your savings account?')

                    if savings.isnumeric():

                        print('${0:.2f} has been added into your savings account.'.format(float(savings)))
                        savingsbal.append(float(savings))
                        atransaction = input('Would you like to make another transaction? Yes or no?')

                        if atransaction == "yes" or atransaction == "y":
                            mainmenu()
                        else:
                            print('\nThank you for choosing Bank of America! Have a nice day!')
                        exit()
                    else: print('You must enter a number.')
            else:print('\nYou must type either checking or savings.')


    elif bank ==  '2' or bank.casefold() == 'withdrawal':
        while True:
            typewithdrawal = input('Would you like to make a withdrawal from your checking or savings account?')

            if typewithdrawal == 'checking':
                while True:
                    checking = float(input('How much money would you like to withdraw from your checking account?'))

                    if checking > sum(checkingbal):
                        print('\nYou only have ${0:,.2f} in your checking account. Please re-enter a smaller amount.'.format(sum(checkingbal)))
                    else:
                        print('${0:,.2f} has been withdrawn from your checking account.'.format(float(checking)))
                        checkingbal.append(float(-checking))

                        atransaction = input('Would you like to make another transaction? Yes or no?')

                        if atransaction == "yes" or atransaction == "y":
                            mainmenu()
                        else:
                            print('\nThank you for choosing Bank of America! Have a nice day!')
                            exit()

            elif typewithdrawal == 'savings':
                while True:
                    savings = float(input('How much money would you like to withdraw from your savings account?'))

                    if savings > sum(savingsbal):
                        print('\nYou only have ${0:,.2f} in your savings account. Please re-enter a smaller amount.'.format(sum(savingsbal)))
                    else:
                        print('${0:,.2f} has been withdrawn from your savings account'.format(float(savings)))
                        savingsbal.append(float(-savings))

                        atransaction = input('Would you like to make another transaction? Yes or no?')

                        if atransaction == "yes" or atransaction == "y":
                            mainmenu()
                        else:
                            print('\nThank you for choosing Bank of America! Have a nice day!')
                            exit()
            else:print('\nYou must type either checking or savings.')



    elif bank == '3' or bank.casefold() == 'transfer':
        while True:
            typetransfer = input('Would you like to transfer money into your checking or savings account?')

            if typetransfer == 'checking':
                while True:
                    checking = float(input('How much money would you like to transfer into your checking account?'))

                    if checking > sum(savingsbal):
                        print('\nYou do not have enough money in your savings account to transfer that amount. Please re-enter a smaller amount.')
                    else:
                        print('${0:,.2f} has been transferred into your checking account.'.format(float(checking)))
                        checkingbal.append(float(checking))
                        savingsbal.append(float(-checking))
                        atransaction = input('Would you like to make another transaction? Yes or no?')

                        if atransaction == "yes" or atransaction == "y":
                            mainmenu()
                        else:
                            print('\nThank you for choosing Bank of America! Have a nice day!')
                        exit()


            elif typetransfer == 'savings':
                while True:
                    savings = float(input('How much money would you like to transfer into your savings account?'))

                    if savings > sum(checkingbal):
                        print('\nYou do not have enough money in your checking account to transfer that amount. Please re-enter a smaller amount.')
                    else:
                        print('${0:,d} has been transferred into your savings account.'.format(int(savings)))
                        savingsbal.append(float(savings))
                        checkingbal.append(float(-savings))
                        atransaction = input('Would you like to make another transaction? Yes or no?')

                        if atransaction == "yes" or atransaction == "y":
                            mainmenu()
                        else:
                            print('\nThank you for choosing Bank of America! Have a nice day!')
                            exit()
            else:
                print('\nYou must type either checking or savings.')

    elif bank == '4' or bank.casefold() == 'balance inquiry':
        while True:
            typebalance = input('Would you like to know the balance of your checking or savings account?')

            if typebalance == 'checking':
                print('The balance of your checking account is ${0:,.2f}'.format(sum(checkingbal)))

                atransaction = input('Would you like to make another transaction? Yes or no?')

                if atransaction == "yes" or atransaction == "y":
                    mainmenu()
                else:
                    print('\nThank you for choosing Bank of America! Have a nice day!')
                    exit()

            elif typebalance == 'savings':
                print('The balance of your savings account is ${0:,.2f}'.format(sum(savingsbal)))

                atransaction = input('Would you like to make another transaction? Yes or no?')

                if atransaction == "yes" or atransaction == "y":
                    mainmenu()
                else:
                    print('\nThank you for choosing Bank of America! Have a nice day!')
                    exit()
            else:print('\nYou must type either checking or savings.')
    else:
            print('\nYou must select by choosing the corresponding number. Please type 1,2,3, or 4')
            mainmenu()

mainmenu()






