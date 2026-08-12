import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def pull_next_card():
    """Used to pull card for hand"""
    card_val = random.choice(cards)
    return card_val

def final_results(users_hand, dealers_hand, users_score, dealers_score):
    """Based off the score of the user and the dealers hand, prints result of draw, win or loss for the user"""
    print(f"  Your final hand: {users_hand}, final score: {users_score}")

    #If the users first 2 cards are 21 (blackjack) then the user will only see the dealers first card
    if users_score == 21 and len(users_hand) == 2:
        print(f"  Computer's final hand: [{dealers_hand[0]}], final score: {dealers_hand[0]}")

        print("Win with a Blackjack!! :P")

    # If the user busts they lose and only get to see the dealers first card
    elif users_score > 21:
        print(f"  Computer's final hand: [{dealers_hand[0]}], final score: {dealers_hand[0]}")

        print("You busted, so you lose ;_;")

    #User gets to see the computers hand to see how the result of the game came to be
    else:
        print(f"  Computer's final hand: {dealers_hand}, final score: {dealers_score}")


        #If the dealer busts the user wins
        if dealers_score > 21:
            print("Dealer busted. You win!")

        #If the user and the dealer have the same score they draw, even if they both have 21
        elif users_score == dealers_score:
            print("Its a draw!")

        #If the user has a higher score than the dealer ( but below 21), User wins
        elif users_score > dealers_score:
            print("You win!")

        #Otherwise the dealer wins
        else:
            print("You lose!")

    return


def computer_draws(computer_current_hand):
    """Used to get the computers hand after user passes"""
    current_score = sum(computer_current_hand)
    while current_score < 17:
        computer_current_hand.append(pull_next_card())
        ace_checker(users_hand)
        current_score = score_of_hand(computer_current_hand)

        if current_score >= 21:
            break
    return computer_current_hand

def ace_checker(current_hand):
    """If the hand has 11 and score is above 21, change 11 to 1 """
    for index, card_value in enumerate(current_hand):
        if sum(current_hand) > 21:
            if card_value == 11:
                current_hand[index] = 1

    return


def display_users_hand(players_hand, players_score, computers_hand):
    """Used to display the users hand and computers first card while drawing cards, also gets new sum of players' hand"""
    players_score = score_of_hand(users_hand)
    print(f"    Your cards: {players_hand},  current score: {players_score}")

    print(f"    Computer's first card: {computers_hand[0]}")
    return players_score



def score_of_hand(hand):
    """Calculate the score of hand"""
    score = 0
    for value in hand:
        score += value
    return score

#Initializing variables
playing_game = True
users_hand = []
dealers_hand = []
users_score = 0
dealers_score = 0

#Beginning prompt if user wants to play Blackjack
start_game = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\' :  ").lower()

#If they choose not to end program
if start_game == "n":
    print("Okay Bye!")
    playing_game = False

#The user will get to play until they want to stop
while playing_game:
    #Start of game print logo
    print(art.logo)

    #Get users hand (two cards)
    users_hand.append(pull_next_card())
    users_hand.append(pull_next_card())

    #Make sure users starting hand is not over 21 (low chance of [11,11])
    ace_checker(users_hand)

    #Create hand for computer/dealer
    dealers_hand.append(pull_next_card())
    dealers_hand.append(pull_next_card())

    #Make sure dealers starting hand is not over 21 (low chance of [11,11])
    ace_checker(dealers_hand)


    #User will only be able to see the first card in the computers hand
    dealers_score = dealers_hand[0]

    #Get the users score
    users_score = display_users_hand(users_hand, users_score, dealers_hand)

    #If the users first 2 cards equal to 21 they win the game
    if users_score == 21:
        final_results(users_hand, dealers_hand, users_score, dealers_score)

    #Otherwise the user can keep drawing until they get to 21 or bust
    else:
        while users_score <= 21:

            #Ask the user if they want to draw another card or pass and have dealer start drawing
            next_card = input("Type \'y\' to get another card, type \'n\' to pass:  ").lower()

            #Add card to users hand and get new score
            if next_card == "y":
                users_hand.append(pull_next_card())
                ace_checker(users_hand)
                users_score = display_users_hand(users_hand, users_score, dealers_hand)

            #They pass and no longer get to draw
            else:
                break


            #if the user gets more than 21 they bust and lose
            if users_score > 21:
                final_results(users_hand, dealers_hand, users_score, dealers_score)
                break



        #If the user didn't bust, the computer will draw cards
        if users_score <= 21:
            dealers_hand = computer_draws(dealers_hand)
            dealers_score = score_of_hand(dealers_hand)
            final_results(users_hand, dealers_hand, users_score, dealers_score)



    #Asks the user if they want to keep playing
    game_next = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\' :  ").lower()
    #If the play does play another game reset the hands and the scores
    if game_next == "y":
        # print("Another one")
        print("\n"*25)
        users_hand = []
        dealers_hand = []
        users_score = 0
        dealers_score = 0
        continue

    #Otherwise say goodbye to player and end program
    else:
        print("Thank you for playing!")
        playing_game = False







