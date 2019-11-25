import math
import random
from random import shuffle


def blackjackdeck():


    cards = [(s, v) for s in ['Hearts', 'Clubs', 'Spades', 'Diamonds']
             for v in [str(i) for i in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']]

    random.shuffle(cards)

    lcard = [item for t in cards for item in t]

    print("\n\tDan's Blackjack Table\n")

    print("\t1. Play a game against the computer")
    print("\t2. Quit")

    blackjack = input("\nWelcome to Dan's Blackjack Table! Please select an option from above.")

    if blackjack == '1':
        print('Okay! Time to test your blackjack skills.')

        while True:
            bet = input(f'\nHow much money would you like to bet on this round? You may bet as much as $500 per round.')

            if bet.isnumeric() and int(bet)<=500 and int(bet)>=1:


                print(f'\nThe dealer has been dealt two cards one which is face up and one face down. The face up card is a {lcard[1]} of {lcard[0]}.')

                print(f'\nYou have been dealt two cards. The first card is a {lcard[3]} of {lcard[2]}.')


                print(f'The second card is a {lcard[5]} of {lcard[4]}.\n')

                JQK = [10]
                A = [1, 11]

                if lcard[3] == 'Jack' or lcard[3] == 'Queen' or lcard[3] == 'King':
                    lcard[3] = JQK[0]

                if lcard[5] == 'Jack' or lcard[5] == 'Queen' or lcard[5] == 'King':
                    lcard[5] = JQK[0]

                if lcard[3] == 'Ace':
                    lcard[3] = A[1]

                if lcard[5] == 'Ace':
                    lcard[5] = A[1]

                if int(lcard[3]) + int(lcard[5]) == 21:
                    print(f'Congratulations you got a blackjack!')
                    print(f'\nThe dealer has completed his hand. His face down card was a {lcard[7]} of {lcard[6]}.')

                    JQK = [10]
                    A = [1, 11]

                    if lcard[1] == 'Jack' or lcard[1] == 'Queen' or lcard[1] == 'King':
                        lcard[1] = JQK[0]

                    if lcard[3] == 'Jack' or lcard[3] == 'Queen' or lcard[3] == 'King':
                        lcard[3] = JQK[0]

                    if lcard[5] == 'Jack' or lcard[5] == 'Queen' or lcard[5] == 'King':
                        lcard[5] = JQK[0]

                    if lcard[3] == 'Ace':
                        lcard[3] = A[1]

                    if lcard[5] == 'Ace':
                        lcard[5] = A[1]

                    if lcard[1] == 'Ace' and lcard[7] != 'Jack' and lcard[7] != 'Queen' and lcard[7] != 'King' and lcard[7] != 10 and lcard[7] != 9 and lcard[7] != 8:
                        lcard[1] = A[0]

                    if lcard[1] == 'Ace' and (lcard[7] == 'Jack' or lcard[7] == 'Queen' or lcard[7] == 'King' or lcard[
                        7] == 10 or lcard[7] == 9 or lcard[7] == 8):
                        lcard[1] = A[1]

                    if lcard[7] == 'Jack' or lcard[7] == 'Queen' or lcard[7] == 'King':
                        lcard[7] = JQK[0]

                    if lcard[7] == 'Ace' and int(lcard[1]) < 6:
                        lcard[7] = A[0]

                    if lcard[7] == 'Ace' and int(lcard[1]) >= 6:
                        lcard[7] = A[1]

                    if int(lcard[1]) + int(lcard[7]) != 21:
                        print(f'\nCongratulations you win {int(lcard[3]) + int(lcard[5])}-{int(lcard[1]) + int(lcard[7])} over the dealer. You win ${round(int(bet) * 1.5)}!')
                        blackjackdeck()
                    else:
                        print(f'\nYou and the dealer both got a blackjack! Your bet of ${int(bet)} has been returned to you.')
                        blackjackdeck()


                stayhit = input('Would you like to stand or hit?')


                if stayhit == 'stand':

                    JQK = [10]
                    A = [1, 11]

                    if lcard[3] == 'Jack' or lcard[3] == 'Queen' or lcard[3] == 'King':
                        lcard[3] = JQK[0]

                    if lcard[5] == 'Jack' or lcard[5] == 'Queen' or lcard[5] == 'King':
                        lcard[5] = JQK[0]

                    if lcard[3] == 'Ace':
                        lcard[3] = A[1]

                    if lcard[5] == 'Ace':
                        lcard[5] = A[1]


                    print(f'\nYou have elected to stand at {int(lcard[3]) + int(lcard[5])}.')
                    print(f'\nThe dealer has completed his hand. His face down card was a {lcard[7]} of {lcard[6]}.')

                    JQK = [10]
                    A = [1, 11]

                    if lcard[1] == 'Jack' or lcard[1] == 'Queen' or lcard[1] == 'King':
                        lcard[1] = JQK[0]

                    if lcard[3] == 'Jack' or lcard[3] == 'Queen' or lcard[3] == 'King':
                        lcard[3] = JQK[0]

                    if lcard[5] == 'Jack' or lcard[5] == 'Queen' or lcard[5] == 'King':
                        lcard[5] = JQK[0]

                    if lcard[3] == 'Ace':
                        lcard[3] = A[1]

                    if lcard[5] == 'Ace':
                        lcard[5] = A[1]

                    if lcard[1] == 'Ace' and lcard[7] != 'Jack' and lcard[7] != 'Queen' and lcard[7] != 'King' and lcard[7] != 10 and lcard[7] != 9 and lcard[7] != 8:
                        lcard[1] = A[0]

                    if lcard[1] == 'Ace' and (lcard[7] == 'Jack' or lcard[7] == 'Queen' or lcard[7] == 'King' or lcard[
                        7] == 10 or lcard[7] == 9 or lcard[7] == 8):
                        lcard[1] = A[1]

                    if lcard[7] == 'Jack' or lcard[7] == 'Queen' or lcard[7] == 'King':
                        lcard[7] = JQK[0]

                    if lcard[7] == 'Ace' and int(lcard[1]) < 6:
                        lcard[7] = A[0]

                    if lcard[7] == 'Ace' and int(lcard[1]) >= 6:
                        lcard[7] = A[1]

                    if int(lcard[1]) + int(lcard[7]) == 21:
                        print(f'\nThe dealer got a blackjack! Sorry you lose ${int(bet)}.')
                        blackjackdeck()

                    elif int(lcard[1]) + int(lcard[7]) > 15:
                        print(f'\nThe dealer has elected to stand at {int(lcard[1]) + int(lcard[7])}.')

                        if int(lcard[1]) + int(lcard[7]) > int(lcard[3]) + int(lcard[5]):
                            print(
                                f'\nThe dealer has outscored you {int(lcard[1]) + int(lcard[7])}-{int(lcard[3]) + int(lcard[5])}. Sorry you lose ${int(bet)}.')
                            blackjackdeck()

                        elif int(lcard[1]) + int(lcard[7]) == int(lcard[3]) + int(lcard[5]):
                            print(
                                f'\nYou tied the dealer {int(lcard[1]) + int(lcard[7])}-{int(lcard[3]) + int(lcard[5])}. Your bet of ${int(bet)} has been returned to you.')
                            blackjackdeck()

                        else:
                            print(
                                f'\nCongratulations! You outscored the dealer {int(lcard[3]) + int(lcard[5])}-{int(lcard[1]) + int(lcard[7])}. You win ${int(bet)}!')
                            blackjackdeck()
                    else:
                        print(
                            f'\nThe dealer elected to hit again. The next card he was dealt was a {lcard[9]} of {lcard[8]}.')

                        JQK = [10]
                        A = [1, 11]

                        if lcard[9] == 'Jack' or lcard[9] == 'Queen' or lcard[9] == 'King':
                            lcard[9] = JQK[0]

                        if lcard[9] == 'Ace':
                            lcard[9] = A[0]

                        if int(lcard[1]) + int(lcard[7]) + int(lcard[9]) > 21:
                            print(f'The dealer busted. You win ${int(bet)}!')
                            blackjackdeck()
                        elif int(lcard[1]) + int(lcard[7]) + int(lcard[9]) > 14:
                            print(
                                f'The dealer has elected to stand at {int(lcard[1]) + int(lcard[7]) + int(lcard[9])}.')

                            if int(lcard[1]) + int(lcard[7]) + int(lcard[9]) > int(lcard[3]) + int(lcard[5]):
                                print(
                                    f'\nThe dealer has outscored you {int(lcard[1]) + int(lcard[7]) + int(lcard[9])}-{int(lcard[3]) + int(lcard[5])}. Sorry you lose ${int(bet)}.')
                                blackjackdeck()

                            elif int(lcard[1]) + int(lcard[7]) + int(lcard[9]) == int(lcard[3]) + int(lcard[5]):
                                print(
                                    f'\nYou tied the dealer {int(lcard[1]) + int(lcard[7]) + int(lcard[9])}-{int(lcard[3]) + int(lcard[5])}. Your bet of ${int(bet)} has been returned to you.')
                                blackjackdeck()

                            else:
                                print(
                                    f'\nCongratulations! You outscored the dealer {int(lcard[3]) + int(lcard[5])}-{int(lcard[1]) + int(lcard[7]) + int(lcard[9])}. You win ${int(bet)}! ')
                                blackjackdeck()
                        else:
                            print(f'\nThe dealer elected to hit again. The next card he was dealt was a {lcard[15]} of {lcard[14]}.')

                            JQK = [10]
                            A = [1, 11]


                            if lcard[15] == 'Jack' or lcard[15] == 'Queen' or lcard[15] == 'King':
                                lcard[15] = JQK[0]

                            if lcard[15] == 'Ace':
                                lcard[15] = A[0]


                            if int(lcard[1]) + int(lcard[7]) + int(lcard[9]) + int(lcard[15]) > 21:
                                print(f'The dealer busted. You win ${int(bet)}!')
                                blackjackdeck()
                            else:
                                print(f'The dealer has elected to stand at {int(lcard[1]) + int(lcard[7]) + int(lcard[9]) + int(lcard[15])}.')

                                if int(lcard[1]) + int(lcard[7]) + int(lcard[9]) + int(lcard[15]) > int(lcard[3]) + int(lcard[5]):
                                    print(
                                        f'\nThe dealer has outscored you {int(lcard[1]) + int(lcard[7]) + int(lcard[9]) + int(lcard[15])}-{int(lcard[3]) + int(lcard[5])}. Sorry you lose ${int(bet)}.')
                                    blackjackdeck()

                                elif int(lcard[1]) + int(lcard[7]) + int(lcard[9]) + int(lcard[15]) == int(lcard[3]) + int(lcard[5]):
                                    print(
                                        f'\nYou tied the dealer {int(lcard[1]) + int(lcard[7]) + int(lcard[9]) + int(lcard[15])}-{int(lcard[3]) + int(lcard[5])}. Your bet of ${int(bet)} has been returned to you.')
                                    blackjackdeck()

                                else:
                                    print(
                                        f'\nCongratulations! You outscored the dealer {int(lcard[3]) + int(lcard[5])}-{int(lcard[1]) + int(lcard[7]) + int(lcard[9]) + int(lcard[15])}. You win ${int(bet)}! ')
                                    blackjackdeck()

                if stayhit == 'hit':

                    print(f'\nThe next card you have been dealt is a {(lcard[11])} of {(lcard[10])}.')

                    JQK = [10]
                    A = [1, 11]

                    if lcard[11] == 'Jack' or lcard[11] == 'Queen' or lcard[11] == 'King':
                        lcard[11] = JQK[0]

                    if lcard[11] == 'Ace':
                        lcard[11] = A[1]

                    if lcard[3] == 'Jack' or lcard[3] == 'Queen' or lcard[3] == 'King':
                        lcard[3] = JQK[0]


                    if lcard[5] == 'Jack' or lcard[5] == 'Queen' or lcard[5] == 'King':
                        lcard[5] = JQK[0]

                    if lcard[3] == 'Ace':
                        lcard[3] = A[1]

                    if lcard[5] == 'Ace':
                        lcard[5] = A[1]

                    if lcard[3] == 11 and (int(lcard[11]) + int(lcard[3]) + int(lcard[5]) > 21):
                        lcard[3] = A[0]

                    if lcard[5] == 11 and (int(lcard[11]) + int(lcard[3]) + int(lcard[5]) > 21):
                        lcard[5] = A[0]


                    if int(lcard[11]) + int(lcard[3]) + int(lcard[5]) > 21:
                        print(f'\n You busted!')
                        print(
                            f'\nThe dealer has completed his hand. His face down card was a {lcard[7]} of {lcard[6]}.')

                        JQK = [10]
                        A = [1, 11]

                        if lcard[1] == 'Jack' or lcard[1] == 'Queen' or lcard[1] == 'King':
                            lcard[1] = JQK[0]

                        if lcard[3] == 'Jack' or lcard[3] == 'Queen' or lcard[3] == 'King':
                            lcard[3] = JQK[0]

                        if lcard[5] == 'Jack' or lcard[5] == 'Queen' or lcard[5] == 'King':
                            lcard[5] = JQK[0]

                        if lcard[3] == 'Ace':
                            lcard[3] = A[1]

                        if lcard[5] == 'Ace':
                            lcard[5] = A[1]

                        if lcard[1] == 'Ace':
                            lcard[1] = A[1]

                        if lcard[7] == 'Jack' or lcard[7] == 'Queen' or lcard[7] == 'King':
                            lcard[7] = JQK[0]

                        if lcard[7] == 'Ace' and int(lcard[1]) < 6:
                            lcard[7] = A[0]

                        if lcard[7] == 'Ace' and int(lcard[1]) >= 6:
                            lcard[7] = A[1]

                        if int(lcard[1]) + int(lcard[7]) == 21:
                            print(f'\nThe dealer got a blackjack! Sorry you lose ${int(bet)}.')
                            blackjackdeck()

                        elif int(lcard[1]) + int(lcard[7]) > 15:
                            print(f'\nThe dealer has elected to stand at {int(lcard[1]) + int(lcard[7])}.')
                            print(f'\nThe dealer wins ${int(bet)}.')
                            blackjackdeck()


                        else:
                            print(
                                f'\nThe dealer elected to hit again. The next card he was dealt was a {lcard[9]} of {lcard[8]}.')

                            if lcard[9] == 'Jack' or lcard[9] == 'Queen' or lcard[9] == 'King':
                                lcard[9] = JQK[0]

                            if lcard[9] == 'Ace':
                                lcard[9] = A[0]

                            if int(lcard[1]) + int(lcard[7]) + int(lcard[9]) > 21:
                                print(f'The dealer busted. Your bet of ${int(bet)} has been returned to you because you and the dealer both busted.')
                                blackjackdeck()
                            else:
                                print(
                                    f'The dealer has elected to stand at {int(lcard[1]) + int(lcard[7]) + int(lcard[9])}.')
                                print(f'\nThe dealer wins ${int(bet)}!')
                                blackjackdeck()

                    else:
                        print(f'\nYou currently stand at {int(lcard[11]) + int(lcard[3]) + int(lcard[5])}.')

                    hitagain = input('Would you like to stand or hit again?')

                    if hitagain == 'hit':

                        JQK = [10]
                        A = [1, 11]

                        if lcard[13] == 'Jack' or lcard[13] == 'Queen' or lcard[13] == 'King':
                            lcard[13] = JQK[0]

                        if lcard[13] == 'Ace':
                            lcard[13] = A[1]

                        if lcard[13] == 11 and (int(lcard[11]) + int(lcard[3]) + int(lcard[5] + int(lcard[13])) > 21):
                            lcard[13] = A[0]

                        print(f'\nThe next card you have been dealt is a {(lcard[13])} of {(lcard[12])}.')

                        if int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13]) > 21:
                            print(f'\n You busted!')
                            print(
                                f'\nThe dealer has completed his hand. His face down card was a {lcard[7]} of {lcard[6]}.')


                            JQK = [10]
                            A = [1, 11]

                            if lcard[1] == 'Jack' or lcard[1] == 'Queen' or lcard[1] == 'King':
                                lcard[1] = JQK[0]

                            if lcard[3] == 'Jack' or lcard[3] == 'Queen' or lcard[3] == 'King':
                                lcard[3] = JQK[0]

                            if lcard[5] == 'Jack' or lcard[5] == 'Queen' or lcard[5] == 'King':
                                lcard[5] = JQK[0]

                            if lcard[3] == 'Ace':
                                lcard[3] = A[1]

                            if lcard[5] == 'Ace':
                                lcard[5] = A[1]

                            if lcard[1] == 'Ace':
                                lcard[1] = A[1]

                            if lcard[7] == 'Jack' or lcard[7] == 'Queen' or lcard[7] == 'King':
                                lcard[7] = JQK[0]

                            if lcard[7] == 'Ace' and int(lcard[1]) < 6:
                                lcard[7] = A[0]

                            if lcard[7] == 'Ace' and int(lcard[1]) >= 6:
                                lcard[7] = A[1]

                            if int(lcard[1]) + int(lcard[7]) > 15:
                                print(f'\nThe dealer has elected to stand at {int(lcard[1]) + int(lcard[7])}.')

                                print(f'\nThe dealer wins ${int(bet)}.')
                                blackjackdeck()
                            else:
                                print(
                                    f'\nThe dealer elected to hit again. The next card he was dealt was a {lcard[9]} of {lcard[8]}.')

                                if lcard[9] == 'Jack' or lcard[9] == 'Queen' or lcard[9] == 'King':
                                    lcard[9] = JQK[0]

                                if lcard[9] == 'Ace':
                                    lcard[9] = A[0]

                                if int(lcard[1]) + int(lcard[7]) + int(lcard[9]) > 21:
                                    print(f'The dealer busted. Your bet of ${int(bet)} has been returned to you because you and the dealer both busted.')
                                    blackjackdeck()
                                else:
                                    print(
                                        f'\nThe dealer has elected to stand at {int(lcard[1]) + int(lcard[7]) + int(lcard[9])}.')

                                    print(f'\nThe dealer wins ${int(bet)}.')
                                    blackjackdeck()


                        else:print(f'\nYou currently stand at {int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13])}.')

                        hitagain2 = input('Would you like to stand or hit again?')

                        if hitagain2 == 'hit':

                                print(f'\nThe next card you have been dealt is a {(lcard[17])} of {(lcard[16])}.')

                                JQK = [10]
                                A = [1, 11]

                                if lcard[17] == 'Ace':
                                    lcard[17] = A[1]

                                if lcard[17] == 11 and (int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13]) + int(lcard[17]) > 21):
                                    lcard[17] = A[0]

                                if lcard[17] == 'Jack' or lcard[17] == 'Queen' or lcard[17] == 'King':
                                    lcard[17] = JQK[0]

                                if  int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13]) + int(lcard[17]) > 21:
                                    print('You busted!')

                                print(
                                    f'\nThe dealer has completed his hand. His face down card was a {lcard[7]} of {lcard[6]}.')

                                JQK = [10]
                                A = [1, 11]

                                if lcard[1] == 'Jack' or lcard[1] == 'Queen' or lcard[1] == 'King':
                                    lcard[1] = JQK[0]

                                if lcard[3] == 'Jack' or lcard[3] == 'Queen' or lcard[3] == 'King':
                                    lcard[3] = JQK[0]

                                if lcard[5] == 'Jack' or lcard[5] == 'Queen' or lcard[5] == 'King':
                                    lcard[5] = JQK[0]

                                if lcard[3] == 'Ace':
                                    lcard[3] = A[1]

                                if lcard[5] == 'Ace':
                                    lcard[5] = A[1]

                                if lcard[1] == 'Ace':
                                    lcard[1] = A[1]

                                if lcard[7] == 'Jack' or lcard[7] == 'Queen' or lcard[7] == 'King':
                                    lcard[7] = JQK[0]

                                if lcard[7] == 'Ace' and int(lcard[1]) < 6:
                                    lcard[7] = A[0]

                                if lcard[7] == 'Ace' and int(lcard[1]) >= 6:
                                    lcard[7] = A[1]

                                if int(lcard[1]) + int(lcard[7]) > 15:
                                    print(f'\nThe dealer has elected to stand at {int(lcard[1]) + int(lcard[7])}.')

                                    if int(lcard[1]) + int(lcard[7]) > int(lcard[11]) + int(lcard[3]) + int(
                                            lcard[5]) + int(lcard[13]) + int(lcard[17]):
                                        print(
                                            f'\nThe dealer has outscored you {int(lcard[1]) + int(lcard[7])}-{int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13]) + int(lcard[17])}. Sorry you lose ${int(bet)}.')
                                        blackjackdeck()

                                    elif int(lcard[1]) + int(lcard[7]) == int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13]) + int(lcard[17]):
                                        print(
                                            f'\nYou tied the dealer {int(lcard[1]) + int(lcard[7])}-{int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13]) + int(lcard[17])}. Your bet of ${int(bet)} has been returned to you.')
                                        blackjackdeck()

                                    else:
                                        print(
                                            f'\nCongratulations! You outscored the dealer {int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13]) + int(lcard[17])}-{int(lcard[1]) + int(lcard[7])}. You win ${int(bet)}!')
                                        blackjackdeck()
                                else:
                                    print(
                                        f'\nThe dealer elected to hit again. The next card he was dealt was a {lcard[9]} of {lcard[8]}.')

                                    if lcard[9] == 'Jack' or lcard[9] == 'Queen' or lcard[9] == 'King':
                                        lcard[9] = JQK[0]

                                    if lcard[9] == 'Ace':
                                        lcard[9] = A[0]

                                    if int(lcard[1]) + int(lcard[7]) + int(lcard[9]) > 21:
                                        print(
                                            f'The dealer busted. Your bet of ${int(bet)} has been returned to you because you and the dealer both busted.')
                                        blackjackdeck()
                                    else:
                                        print(
                                            f'The dealer has elected to stand at {int(lcard[1]) + int(lcard[7]) + int(lcard[9])}.')

                                        if int(lcard[1]) + int(lcard[7]) + int(lcard[9]) > int(lcard[11]) + int(
                                                lcard[3]) + int(lcard[5]) + int(lcard[13]) + int(lcard[17]):
                                            print(
                                                f'\nThe dealer has outscored you {int(lcard[1]) + int(lcard[7]) + int(lcard[9])}-{int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13])  + int(lcard[17]) }. Sorry you lose ${int(bet)}.')
                                            blackjackdeck()

                                        elif int(lcard[1]) + int(lcard[7]) + int(lcard[9]) == int(lcard[11]) + int(
                                                lcard[3]) + int(lcard[5]) + int(lcard[13]) + int(lcard[17]):
                                            print(
                                                f'\nYou tied the dealer {int(lcard[1]) + int(lcard[7]) + int(lcard[9])}-{int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13])  + int(lcard[17])}. Your bet of ${int(bet)} has been returned to you.')
                                            blackjackdeck()

                                        else:
                                            print(
                                                f'\nCongratulations! You outscored the dealer {int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13])  + int(lcard[17])}-{int(lcard[1]) + int(lcard[7]) + int(lcard[9])}. You win ${int(bet)}! ')
                                            blackjackdeck()

                        if hitagain2 == 'stand':

                                print(
                                f'\nThe dealer has completed his hand. His face down card was a {lcard[7]} of {lcard[6]}.')

                                JQK = [10]
                                A = [1, 11]

                                if lcard[1] == 'Jack' or lcard[1] == 'Queen' or lcard[1] == 'King':
                                    lcard[1] = JQK[0]

                                if lcard[3] == 'Jack' or lcard[3] == 'Queen' or lcard[3] == 'King':
                                    lcard[3] = JQK[0]

                                if lcard[5] == 'Jack' or lcard[5] == 'Queen' or lcard[5] == 'King':
                                    lcard[5] = JQK[0]

                                if lcard[3] == 'Ace':
                                    lcard[3] = A[1]

                                if lcard[5] == 'Ace':
                                    lcard[5] = A[1]

                                if lcard[1] == 'Ace':
                                    lcard[1] = A[1]

                                if lcard[7] == 'Jack' or lcard[7] == 'Queen' or lcard[7] == 'King':
                                    lcard[7] = JQK[0]

                                if lcard[7] == 'Ace' and int(lcard[1]) < 6:
                                    lcard[7] = A[0]

                                if lcard[7] == 'Ace' and int(lcard[1]) >= 6:
                                    lcard[7] = A[1]


                                if int(lcard[1]) + int(lcard[7]) == 21:
                                    print(f'\nThe dealer got a blackjack! Sorry you lose {int(lcard[1]) + int(lcard[7])}-{int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13])}. The dealer wins ${round(int(bet) * 1.5)} ')
                                    blackjackdeck()

                                elif int(lcard[1]) + int(lcard[7]) > 15:
                                    print(f'\nThe dealer has elected to stand at {int(lcard[1]) + int(lcard[7])}.')

                                    if int(lcard[1]) + int(lcard[7]) > int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13]):
                                        print(
                                            f'\nThe dealer has outscored you {int(lcard[1]) + int(lcard[7])}-{int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13])}. Sorry you lose ${int(bet)}.')
                                        blackjackdeck()

                                    elif int(lcard[1]) + int(lcard[7]) == int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13]):
                                        print(
                                            f'\nYou tied the dealer {int(lcard[1]) + int(lcard[7])}-{int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13])}. Your bet of ${int(bet)} has been returned to you.')
                                        blackjackdeck()

                                    else:
                                        print(
                                            f'\nCongratulations! You outscored the dealer {int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13])}-{int(lcard[1]) + int(lcard[7])}. You win ${int(bet)}!')
                                        blackjackdeck()
                                else:
                                    print(
                                        f'\nThe dealer elected to hit again. The next card he was dealt was a {lcard[9]} of {lcard[8]}.')

                                    if lcard[9] == 'Jack' or lcard[9] == 'Queen' or lcard[9] == 'King':
                                        lcard[9] = JQK[0]

                                    if lcard[9] == 'Ace':
                                        lcard[9] = A[0]

                                    if int(lcard[1]) + int(lcard[7]) + int(lcard[9]) > 21:
                                        print(f'The dealer busted. You win ${int(bet)}!')
                                        blackjackdeck()
                                    else:
                                        print(
                                        f'The dealer has elected to stand at {int(lcard[1]) + int(lcard[7]) + int(lcard[9])}.')

                                        if int(lcard[1]) + int(lcard[7]) + int(lcard[9]) > int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13]):
                                            print(
                                                f'\nThe dealer has outscored you {int(lcard[1]) + int(lcard[7]) + int(lcard[9])}-{int(lcard[3]) + int(lcard[5]) + int(lcard[11]) + int(lcard[13])}. Sorry you lose ${int(bet)}.')
                                            blackjackdeck()

                                        elif int(lcard[1]) + int(lcard[7]) + int(lcard[9]) == int(lcard[11]) + int(lcard[3]) + int(lcard[5]) + int(lcard[13]):
                                            print(
                                                f'\nYou tied the dealer {int(lcard[1]) + int(lcard[7]) + int(lcard[9])}-{int(lcard[3]) + int(lcard[5])  + int(lcard[11]) + int(lcard[13])}. Your bet of ${int(bet)} has been returned to you.')
                                            blackjackdeck()

                                        else:
                                            print(
                                                f'\nCongratulations! You outscored the dealer {int(lcard[3]) + int(lcard[5]) + int(lcard[11]) + int(lcard[13])}-{int(lcard[1]) + int(lcard[7]) + int(lcard[9])}. You win ${int(bet)}! ')
                                            blackjackdeck()

                    if hitagain == 'stand':
                        print(f'\nYou have elected to stand at {int(lcard[11]) + int(lcard[3]) + int(lcard[5])}.')
                        print(
                            f'\nThe dealer has completed his hand. His face down card was a {lcard[7]} of {lcard[6]}.')

                        JQK = [10]
                        A = [1, 11]

                        if lcard[1] == 'Jack' or lcard[1] == 'Queen' or lcard[1] == 'King':
                            lcard[1] = JQK[0]

                        if lcard[3] == 'Jack' or lcard[3] == 'Queen' or lcard[3] == 'King':
                            lcard[3] = JQK[0]

                        if lcard[5] == 'Jack' or lcard[5] == 'Queen' or lcard[5] == 'King':
                            lcard[5] = JQK[0]

                        if lcard[11] == 'Jack' or lcard[11] == 'Queen' or lcard[11] == 'King':
                            lcard[11] = JQK[0]

                        if lcard[11] == 'Ace':
                            lcard[11] = A[1]

                        if lcard[3] == 'Ace':
                            lcard[3] = A[1]

                        if lcard[5] == 'Ace':
                            lcard[5] = A[1]

                        if lcard[1] == 'Ace':
                            lcard[1] = A[1]

                        if lcard[7] == 'Jack' or lcard[7] == 'Queen' or lcard[7] == 'King':
                            lcard[7] = JQK[0]

                        if lcard[7] == 'Ace' and int(lcard[1]) < 6:
                            lcard[7] = A[0]

                        if lcard[7] == 'Ace' and int(lcard[1]) >= 6:
                            lcard[7] = A[1]

                        if int(lcard[1]) + int(lcard[7]) > 15:
                            print(f'\nThe dealer has elected to stand at {int(lcard[1]) + int(lcard[7])}.')

                            if int(lcard[1]) + int(lcard[7]) > int(lcard[3]) + int(lcard[5]) + int(lcard[11]):
                                print(
                                    f'\nThe dealer has outscored you {int(lcard[1]) + int(lcard[7])}-{int(lcard[3]) + int(lcard[5]) + int(lcard[11])}. Sorry you lose ${int(bet)}.')
                                blackjackdeck()

                            elif int(lcard[1]) + int(lcard[7]) == int(lcard[3]) + int(lcard[5]) + int(lcard[11]):
                                print(
                                    f'\nYou tied the dealer {int(lcard[1]) + int(lcard[7])}-{int(lcard[3]) + int(lcard[5]) + int(lcard[11])}. Your bet of ${int(bet)} has been returned to you.')
                                blackjackdeck()

                            else:
                                print(
                                    f'\nCongratulations! You outscored the dealer {int(lcard[3]) + int(lcard[5]) + int(lcard[11])}-{int(lcard[1]) + int(lcard[7])}. You win ${int(bet)}!')
                                blackjackdeck()
                        else:
                            print(
                                f'\nThe dealer elected to hit again. The next card he was dealt was a {lcard[9]} of {lcard[8]}.')

                            JQK = [10]
                            A = [1, 11]

                            if lcard[9] == 'Jack' or lcard[9] == 'Queen' or lcard[9] == 'King':
                                lcard[9] = JQK[0]

                            if lcard[9] == 'Ace':
                                lcard[9] = A[0]

                            if lcard[1] == 'Jack' or lcard[1] == 'Queen' or lcard[1] == 'King':
                                lcard[1] = JQK[0]

                            if lcard[3] == 'Jack' or lcard[3] == 'Queen' or lcard[3] == 'King':
                                lcard[3] = JQK[0]

                            if lcard[5] == 'Jack' or lcard[5] == 'Queen' or lcard[5] == 'King':
                                lcard[5] = JQK[0]

                            if lcard[11] == 'Jack' or lcard[11] == 'Queen' or lcard[11] == 'King':
                                lcard[11] = JQK[0]

                            if lcard[11] == 'Ace':
                                lcard[11] = A[1]

                            if lcard[3] == 'Ace':
                                lcard[3] = A[1]

                            if lcard[5] == 'Ace':
                                lcard[5] = A[1]

                            if lcard[1] == 'Ace':
                                lcard[1] = A[1]

                            if lcard[7] == 'Jack' or lcard[7] == 'Queen' or lcard[7] == 'King':
                                lcard[7] = JQK[0]

                            if lcard[7] == 'Ace' and int(lcard[1]) < 6:
                                lcard[7] = A[0]

                            if lcard[7] == 'Ace' and int(lcard[1]) >= 6:
                                lcard[7] = A[1]

                            if int(lcard[1]) + int(lcard[7]) + int(lcard[9]) > 21:
                                print(f'The dealer busted. You win ${int(bet)}!')
                                blackjackdeck()
                            else:
                                print(
                                    f'The dealer has elected to stand at {int(lcard[1]) + int(lcard[7]) + int(lcard[9])}.')

                                if int(lcard[1]) + int(lcard[7]) + int(lcard[9]) > int(lcard[3]) + int(lcard[5])+ int(lcard[11]):
                                    print(
                                        f'\nThe dealer has outscored you {int(lcard[1]) + int(lcard[7]) + int(lcard[9])}-{int(lcard[3]) + int(lcard[5])+ int(lcard[11])}. Sorry you lose ${int(bet)}.')
                                    blackjackdeck()

                                elif int(lcard[1]) + int(lcard[7]) + int(lcard[9]) == int(lcard[3]) + int(lcard[5])+ int(lcard[11]):
                                    print(
                                        f'\nYou tied the dealer {int(lcard[1]) + int(lcard[7]) + int(lcard[9])}-{int(lcard[3]) + int(lcard[5]) + int(lcard[11])}. Your bet of ${int(bet)} has been returned to you.')
                                    blackjackdeck()

                                else:
                                    print(
                                        f'\nCongratulations! You outscored the dealer {int(lcard[3]) + int(lcard[5])+ int(lcard[11])}-{int(lcard[1]) + int(lcard[7]) + int(lcard[9])}. You win ${int(bet)}! ')
                                    blackjackdeck()

            elif bet.isnumeric() and int(bet) > 500:
                print(f'\n You can not bet more than $500 per round. Please wager a smaller amount.')

            else:   print(f'\nTo enter your bet please enter an integer between 1 and 500.')
    elif blackjack == '2':
        exit()
blackjackdeck()



