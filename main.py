import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def user(cards):
    return(random.choice(cards))

def computer(cards):
    if(len(computer_cards ) == 0):
        return(random.choice(cards))
    elif(sum(computer_cards) >= 10):
        return((sum(computer_cards))/2)
    else:
        return(random.choice(cards))

def sum_greater(cards):
    print('your sum is greater then 21')
    print('your sum is', sum(user_cards))
    a = random.choice([1, 2, 3, 4])
    for i in range(a):
        computer_cards.append(computer(cards))
    print('computer cards are', computer_cards )

def computer_input(cards):
    a = random.choice([1, 2, 3, 4])
    for i in range(a):
        computer_cards.append(computer(cards))
    print('computer cards are', computer_cards)

def check():
    if sum(user_cards) > 21 and sum(computer_cards) > 21 :
        print('you both lost the game')

    elif sum(user_cards) > 21 and sum(computer_cards)  <= 21 :
        print('computer won the game')

    elif sum(user_cards) <= 21 and sum(computer_cards)  > 21 :
        print('you won the game')

    elif sum(user_cards) > sum(computer_cards) :
        print('you won the game')

    elif sum(user_cards) < sum(computer_cards) :
        print('computer won the game')
    else:
        print('its draw')

while True:

    user_cards = []
    computer_cards = []

    n = input('would you like to play the game y or n')

    if len(user_cards) == 0 and n.lower() == 'n' :
        exit()

    if len(user_cards) == 0 and n.lower() == 'y' :
        user_cards.append(user(cards))
        user_cards.append(user(cards))
        computer_cards.append(computer(cards))
        print(user_cards, 'sum of your card is ', sum(user_cards))
        print(computer_cards, 'sum of computer card is ', sum(computer_cards))

        if sum(user_cards) > 21:
            sum_greater(cards)
            check()
            continue

    while sum(user_cards) < 21:
        deal_more_cards = input('Want more cards?')
        if deal_more_cards.lower()=='y':
            user_cards.append(user(cards))
        else:
            computer_input(cards)
            check()
            break