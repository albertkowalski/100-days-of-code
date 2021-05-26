import random
import art

print(art.logo)
player_cards = []
dealer_cards = []


def show_card(card_index):
    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K"]
    return cards[card_index]


def get_card_index():
    return random.randint(0, 12)


def get_card_value(card_index, hand_value):
    values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_value = values[card_index]
    if card_index == 0 and hand_value > 10:
        card_value = 1
    return card_value


def initial_deal():
    player_cards.append(get_card_index())
    player_cards.append(get_card_index())
    dealer_cards.append(get_card_index())


initial_deal()
print(
    f"Your hand is {show_card(player_cards[0])} {show_card(player_cards[1])} and hand value is {(get_card_value(player_cards[0], 0) + (get_card_value(player_cards[1], (get_card_value(player_cards[0], 0)))))} "
    f"and opponent is {show_card(dealer_cards[0])}")
