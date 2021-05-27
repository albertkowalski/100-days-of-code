import random
import art
import os
import time


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_card(card_index):
    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K"]
    return cards[card_index]


def get_card_index():
    return random.randint(0, 12)


def get_card_value(card_index):
    values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_value = values[card_index]
    return card_value


def get_hand_value(cards):
    cards_value = 0
    aces = cards.count(0)
    for card in cards:
        if not card == 0:
            cards_value += get_card_value(card)
    if cards_value <= 21 - aces and aces > 0:
        if cards_value + (aces - 1) + get_card_value(0) <= 21:
            cards_value += + aces + 10
        else:
            cards_value += aces
    return cards_value


def show_hand(player, hand):
    cards = []
    for card in hand:
        cards.append(show_card(card))
    print(f"{player} hand:")
    print(*cards)
    print(f"Value of player hand is: {get_hand_value(hand)}")


def in_game(deck):
    if get_hand_value(deck) <= 21:
        return True
    else:
        return False


def initial_deal():
    player_cards.append(get_card_index())
    player_cards.append(get_card_index())
    dealer_cards.append(get_card_index())


def draw_card(deck):
    deck.append(get_card_index())


def show_decks(delay):
    print(art.logo)
    show_hand("Player", player_cards)
    show_hand("Dealer", dealer_cards)
    time.sleep(delay)


keep_playing = True
while keep_playing:
    player_cards = []
    dealer_cards = []
    initial_deal()
    while in_game(player_cards) and in_game(dealer_cards):
        show_decks(0)
        decision = input("Do you want to draw a card 'y' or pass 'n' ? ")
        while not (decision == 'n' or decision == 'y'):
            decision = input("Wrong input! Type 'y' to draw a card and 'n' if you want to pass")
        if decision == 'y':
            draw_card(player_cards)
        if decision == 'n':
            while get_hand_value(player_cards) > get_hand_value(dealer_cards) and get_hand_value(dealer_cards) < 17:
                draw_card(dealer_cards)
                show_decks(2)
            break
        cls()
    if not in_game(player_cards):
        cls()
        show_decks(0)
        print("You got more than 21!! You lost!")
    elif not in_game(dealer_cards):
        cls()
        show_decks(0)
        print("Dealer have more than 21!! You won!")
    elif get_hand_value(player_cards) > get_hand_value(dealer_cards):
        print("You won!")
    elif get_hand_value(player_cards) == get_hand_value(dealer_cards):
        print("Draw")
    else:
        print("You lost!")
    decision = input("Do You want to play again? Type 'y' or 'n'")
    while not (decision == 'y' or decision == 'n'):
        decision = input("Please pick 'y' or 'n'")
    if decision == 'n':
        keep_playing = False
