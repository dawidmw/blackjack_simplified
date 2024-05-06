import os
import random
import sys
import time

def check_score(user, npc):
    total_user = sum(user)
    total_npc = sum(npc)
    if total_user > total_npc:
        print(f"You win with a score of {total_user} against croupier's {total_npc}. Croupier's hand: {npc}.")
        play_again()
    elif total_npc > total_user:
        print(f"You lose against the croupier. Your score: {total_user}. Croupier's score: {total_npc}. Croupier's hand: {npc}.")
        play_again()
    elif total_user == total_npc:
        print(f"It's a draw! Your hand: {user}. Croupier's hand: {npc}.")
        play_again()
        
def bust_croupier(total_npc):
    print(f"Croupier's score: {sum(total_npc)}")
    print(f"Croupier's bust! Their score is higher than 21. Their hand: {total_npc}.")
    print()
    print("You win, congratulations!")
    play_again()

def deal_cards(deck, cards):
    if deck:
        random_card = random.choice(cards)
        if random_card == 11 and (sum(deck) + random_card) > 21:
            random_card = 1
        deck.append(random_card)
    else:
        for _ in range(2):
            random_card = random.choice(cards)
            if random_card == 11 and (sum(deck) + random_card) > 21:
                random_card = 1
            deck.append(random_card)
    return deck

def play_again():
    player_choice = input("Do you want to play again (y/n)? ").lower()
    if player_choice == "y":
        main()
    elif player_choice == "n":
        sys.exit()

def show_npc_cards(npc_deck):
    new_list = []
    cards_with_one_hidden = len(npc_deck)-1
    for card in range(cards_with_one_hidden):
        new_list.append(npc_deck[card])
    print(f"Croupier's cards: {new_list}")
    print()
    return new_list
    
def show_user_cards(user_deck):
    print(f"Your cards: {user_deck}")
    print(f"Current score: {sum(user_deck)}")
    print()
    
def welcome():
    os.system('cls')
    print("Welcome to Blackjack.")
    time.sleep(1)
    print()



def main():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    welcome()

    user_cards = []
    npc_cards = []

    # initial 2 cards deal
    user_cards = deal_cards(user_cards, cards)
    show_user_cards(user_cards)
    npc_cards = deal_cards(npc_cards, cards)
    show_npc_cards(npc_cards)
    

    while True:

        ask_for_another = input("Type 'a' to get another card, type 'p' to pass: ")
        os.system('cls')
        
        if ask_for_another == "a":
            deal_cards(user_cards, cards)
            show_user_cards(user_cards)
            if sum(user_cards) > 21:
                print(f"Your score: {sum(user_cards)}")
                print("You bust! Your score is higher than 21. Croupies wins.")
                play_again()
            deal_cards(npc_cards, cards)
            if sum(npc_cards) < 17:
                deal_cards(npc_cards, cards)
                show_npc_cards(npc_cards)
            elif sum(npc_cards) >= 17:
                show_npc_cards(npc_cards)
                continue
            elif sum(npc_cards) > 21:
                bust_croupier(npc_cards)
            show_npc_cards(npc_cards)

        elif ask_for_another == "p":
            while sum(npc_cards) < 17:
                deal_cards(npc_cards, cards)
            if sum(npc_cards) > 21:
                bust_croupier(npc_cards)
            check_score(user_cards, npc_cards)


if __name__ == "__main__":

    choice = input("Do you want to play a game of blackjack (y/n)? ").lower()
    if choice == "y":
        main()
    elif choice == "n":
        sys.exit()
